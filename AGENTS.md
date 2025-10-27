# AGENTS.md

## 📘 Project Overview
**Project Name:** C14MA  
**Repository:** [GitHub → C14MA]  

This project aims to build a curated **GeoJSON database** of all known **radiocarbon (¹⁴C) records** located within **Morocco**, extracted from the **top 10 global radiocarbon databases**, and create a single-page academic-grade visual explorer called **`data-explorer.html`**.

Final deliverables:
- `Morocco_c14_data.geojson`
- `data-explorer.html`

All work for this project must occur **only inside the `C14MA` GitHub repository**.

---

## Objectives

1. **Collect**
   - Automatically fetch radiocarbon records from the **top 10 reputable databases**, including:
     1. PEOPLE 3000 (p3k14c)
     2. Canadian Archaeological Radiocarbon Database (CARD)
     3. Oxford Radiocarbon Accelerator Unit (ORAU)
     4. CBA Radiocarbon Index (UK & Ireland)
     5. NOSAMS Public Radiocarbon Datasets
     6. IntCal/INTIMATE Database
     7. Radiocarbon Palaeoclimate Database (Reimer et al.)
     8. R_Combine (European compilation)
     9. Open Context Radiocarbon datasets
     10. XRONOS.ch (Swiss Radiocarbon & Archaeological contexts)

   - Query or scrape only records with **geographical coordinates** or **site locations** within **Morocco**.

2. **Normalize**
   - Standardize the dataset schema into GeoJSON feature format:
     ```json
     {
       "type": "Feature",
       "geometry": { "type": "Point", "coordinates": [longitude, latitude] },
       "properties": {
         "site_name": "",
         "lab_code": "",
         "c14_age_bp": "",
         "c14_error": "",
         "material_dated": "",
         "context": "",
         "database_source": "",
         "reference": "",
         "notes": ""
       }
     }
     ```
   - Remove duplicates and harmonize coordinate precision.
   - Validate chronological metadata and discard malformed records.
   - Ensure the **GeoJSON file follows professional standards**, learning from the best practices used in other archaeological and scientific open-data projects (e.g., P3K14C, CARD, and Open Context).

3. **Store**
   - Export the unified dataset as `Morocco_c14_data.geojson`.
   - Include all site-level metadata in `properties`.

4. **Visualize**
   - Build a professional HTML5 page `data-explorer.html`:
     - Load the GeoJSON dynamically with Leaflet.js.
     - Add base map (Esri Satellite).
     - Add cluster markers for sites.
     - Popup on click → show site name, age BP, lab code, material, and source.
     - Include filters (age range, material type, source database).
     - Include a mini summary: total number of samples + number of sites.
     - Use minimal inline CSS and JS, academic color palette (neutral, readable).
     - Responsive layout (works on mobile).

---

## Technical Constraints

- **Files only:** `Morocco_c14_data.geojson`, `data-explorer.html`
- **Libraries allowed:** Leaflet.js, D3.js (optional), Turf.js (optional)
- **No external build tools** (pure HTML + inline JS/CSS)
- **All data must be open-access** or properly credited via metadata
- **Citation field** in properties must include full bibliographic reference or DOI if available
- **All commits and collaboration** must be done through the official **`C14MA` GitHub repository**

---

## Evaluation Criteria

✅ Data accuracy (valid Morocco coordinates, clean metadata)  
✅ Proper merging & standardization of attributes  
✅ Compact, readable GeoJSON (professionally structured)  
✅ Professional interactive visualization suitable for academic use  
✅ Two-file output only  
✅ Repository compliance (`C14MA` GitHub project)

---

## Suggested Workflow

1. **Crawler agent:** Collect and filter data (Morocco only).  
2. **Normalizer agent:** Harmonize schema into unified GeoJSON, following professional standards.  
3. **Validator agent:** Check for duplicates, missing fields, or coordinate issues.  
4. **Frontend agent:** Build `data-explorer.html` with Leaflet interface and filters.  
5. **Supervisor agent:** Ensure both deliverables are complete, valid, and lightweight (<10 MB total).  
6. **Commit agent:** Push final files to the `C14MA` GitHub repository and verify repository integrity.
