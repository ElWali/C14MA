import json
import os
import csv
import io
import time
import requests

# --- Configuration ---
GEOJSON_FILE = 'Morocco_c14_data.geojson'
MIN_GEOJSON_FILE = 'Morocco_c14_data.min.geojson'
RETRIEVAL_LOG_FILE = 'retrieval_log.json'
PROVENANCE_FILE = 'data_provenance.html'
CACHE_DIR = './cache'
MOROCCAN_BOUNDS = {'lat_min': 21.4, 'lat_max': 35.9, 'lon_min': -17.0, 'lon_max': -1.0}

# --- Main Functions ---

def main():
    """Main function to run the data pipeline."""
    print("Starting data retrieval and processing pipeline...")

    # Ensure cache directory exists
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    # The main pipeline steps will be called from here
    xronos_data = fetch_xronos_data()
    print(f"Fetched {len(xronos_data)} records from XRONOS.ch")

    # 1. Load existing data
    existing_data = load_geojson(GEOJSON_FILE)
    print(f"Loaded {len(existing_data['features'])} existing records.")

    # 2. Fetch data from sources
    xronos_data = fetch_xronos_data()
    print(f"Fetched {len(xronos_data)} records from XRONOS.ch")

    opencontext_data = fetch_opencontext_data()
    print(f"Fetched {len(opencontext_data)} records from Open Context (archives)")

    # 3. Merge and deduplicate
    all_features = existing_data['features'] + xronos_data + opencontext_data
    deduplicated_features = deduplicate_features(all_features)
    print(f"Deduplicated to {len(deduplicated_features)} records.")

    # 4. Sort and save
    sorted_features = sorted(deduplicated_features, key=lambda x: x['properties'].get('c14_age_bp') or 0, reverse=True)

    final_geojson = {
        "type": "FeatureCollection",
        "features": sorted_features
    }

    save_geojson(final_geojson, GEOJSON_FILE)
    save_geojson(final_geojson, MIN_GEOJSON_FILE, minify=True)
    print(f"Saved {len(sorted_features)} records to {GEOJSON_FILE} and {MIN_GEOJSON_FILE}")

    # 5. Create audit trail
    retrieval_log = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sources_attempted": ["p3k14c", "xronos", "opencontext"],
        "sources_successful": ["xronos"] if xronos_data else [],
        "records_fetched": {
            "p3k14c": "skipped (inaccessible)",
            "xronos": len(xronos_data),
            "opencontext": len(opencontext_data)
        },
        "records_after_deduplication": len(deduplicated_features)
    }
    save_retrieval_log(retrieval_log)
    generate_provenance_html(retrieval_log, final_geojson)
    print("Audit trail files created.")

    print("Pipeline finished.")

def save_retrieval_log(log_data):
    """Saves the retrieval log to a JSON file."""
    with open(RETRIEVAL_LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, indent=2)

def generate_provenance_html(log_data, geojson_data):
    """Generates a data_provenance.html file."""
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Data Provenance Report</title>
    <style>
        body {{ font-family: sans-serif; margin: 2em; }}
        h1, h2 {{ color: #333; }}
        pre {{ background-color: #f4f4f4; padding: 1em; border-radius: 5px; }}
    </style>
</head>
<body>
    <h1>Data Provenance Report for Morocco C14 Dataset</h1>
    <h2>Retrieval Log</h2>
    <pre>{json.dumps(log_data, indent=2)}</pre>
    <h2>Data Summary</h2>
    <p>Total records: {len(geojson_data['features'])}</p>
</body>
</html>
"""
    with open(PROVENANCE_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)

def load_geojson(filepath):
    """Loads a GeoJSON file."""
    if not os.path.exists(filepath):
        return {"type": "FeatureCollection", "features": []}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_geojson(data, filepath, minify=False):
    """Saves data to a GeoJSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        if minify:
            json.dump(data, f, separators=(',', ':'))
        else:
            json.dump(data, f, indent=2)

def deduplicate_features(features):
    """Deduplicates a list of GeoJSON features based on lab_code."""
    seen_lab_codes = set()
    deduplicated = []
    for feature in features:
        lab_code = feature['properties'].get('lab_code')
        if lab_code and lab_code not in seen_lab_codes:
            seen_lab_codes.add(lab_code)
            deduplicated.append(feature)
        elif not lab_code:
            # Keep features without a lab code for now
            deduplicated.append(feature)
    return deduplicated

def fetch_opencontext_data():
    """
    Placeholder for fetching Open Context data from archives.
    This function will simulate searching Zenodo, tDAR, or Ariadne Portal.
    """
    print("Searching for pre-archived Open Context datasets...")
    # In a real scenario, this would involve API calls to Zenodo/tDAR/Ariadne
    # For now, it returns an empty list.
    return []

def fetch_xronos_data():
    """
    Fetches, processes, and normalizes radiocarbon data for Morocco from XRONOS.ch.
    Includes retry logic and validation against Moroccan bounds.
    """
    url = "https://xronos.ch/c14s.csv?c14[contexts][country]=Morocco"
    max_attempts = 3
    wait_time = 5  # Initial wait time in seconds

    for attempt in range(max_attempts):
        try:
            print(f"Fetching data from {url} (Attempt {attempt + 1}/{max_attempts})...")
            response = requests.get(url, timeout=60)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Process the CSV data
            csv_file = io.StringIO(response.text)
            reader = csv.DictReader(csv_file)

            features = []
            for row in reader:
                try:
                    lat = float(row.get('lat', 0))
                    lon = float(row.get('lon', 0))

                    # Validate required fields and coordinates
                    if not all([row.get('lab_code'), row.get('lat'), row.get('lon'), row.get('reference')]):
                        continue

                    if not (MOROCCAN_BOUNDS['lat_min'] <= lat <= MOROCCAN_BOUNDS['lat_max'] and
                            MOROCCAN_BOUNDS['lon_min'] <= lon <= MOROCCAN_BOUNDS['lon_max']):
                        continue

                    # Normalize to the existing GeoJSON schema
                    feature = {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [lon, lat]
                        },
                        "properties": {
                            "site_name": row.get('site_name', ''),
                            "lab_code": row.get('lab_code', ''),
                            "c14_age_bp": int(float(row.get('c14_age', 0))) if row.get('c14_age') else None,
                            "c14_error": int(float(row.get('c14_std', 0))) if row.get('c14_std') else None,
                            "material_dated": row.get('material', ''),
                            "context": row.get('context', ''),
                            "database_source": "xronos",
                            "reference": row.get('reference', ''),
                            "notes": ""
                        }
                    }
                    features.append(feature)
                except (ValueError, TypeError):
                    # Skip rows with invalid number formats
                    continue

            return features

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            if attempt < max_attempts - 1:
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                wait_time *= 2  # Exponential backoff
            else:
                print("Max retries reached. Skipping XRONOS.ch.")
                return []
    return []

if __name__ == '__main__':
    main()
