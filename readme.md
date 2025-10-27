# C14MA: A Curated Radiocarbon Database for Morocco

| English | <div dir="rtl">Arabic</div> |
|---|---|
| C14MA is a specialized open-source project dedicated to creating a comprehensive and curated GeoJSON database of all known radiocarbon (¹⁴C) records within Morocco. The project aggregates data from the world's top 10 radiocarbon databases, standardizes the information, and presents it through a user-friendly, interactive data explorer. This initiative aims to provide researchers, archaeologists, and historians with a reliable and accessible tool for analyzing chronological data in the region. | <div dir="rtl">C14MA هو مشروع متخصص مفتوح المصدر يهدف إلى إنشاء قاعدة بيانات GeoJSON شاملة ومنسقة لجميع سجلات الكربون المشع (¹⁴C) المعروفة داخل المغرب. يقوم المشروع بتجميع البيانات من أكبر 10 قواعد بيانات للكربون المشع في العالم، وتوحيد المعلومات، وتقديمها من خلال مستكشف بيانات تفاعلي وسهل الاستخدام. تهدف هذه المبادرة إلى تزويد الباحثين وعلماء الآثار والمؤرخين بأداة موثوقة وسهلة الوصول لتحليل البيانات الزمنية في المنطقة.</div> |

---

## Final Deliverables | <div dir="rtl">المخرجات النهائية</div>

| English | <div dir="rtl">Arabic</div> |
|---|---|
| The project will result in two main files: <br> 1. **`Morocco_c14_data.geojson`**: A standardized GeoJSON file containing all the collected radiocarbon records from Morocco. <br> 2. **`data-explorer.html`**: A single-page, professional-grade web application for visualizing and interacting with the GeoJSON data. | <div dir="rtl">سينتج عن المشروع ملفان رئيسيان: <br> 1. **`Morocco_c14_data.geojson`**: ملف GeoJSON موحد يحتوي على جميع سجلات الكربون المشع التي تم جمعها من المغرب. <br> 2. **`data-explorer.html`**: تطبيق ويب احترافي من صفحة واحدة لتصور بيانات GeoJSON والتفاعل معها.</div> |

---

## Data Sources | <div dir="rtl">مصادر البيانات</div>

| English | <div dir="rtl">Arabic</div> |
|---|---|
| The data is collected and aggregated from the following top 10 global radiocarbon databases: | <div dir="rtl">يتم جمع البيانات وتجميعها من أفضل 10 قواعد بيانات عالمية للكربون المشع التالية:</div> |
| - PEOPLE 3000 (p3k14c)<br>- Canadian Archaeological Radiocarbon Database (CARD)<br>- Oxford Radiocarbon Accelerator Unit (ORAU)<br>- CBA Radiocarbon Index (UK & Ireland)<br>- NOSAMS Public Radiocarbon Datasets<br>- IntCal/INTIMATE Database<br>- Radiocarbon Palaeoclimate Database (Reimer et al.)<br>- R_Combine (European compilation)<br>- Open Context Radiocarbon datasets<br>- XRONOS.ch (Swiss Radiocarbon & Archaeological contexts) | <div dir="rtl">- PEOPLE 3000 (p3k14c)<br>- Canadian Archaeological Radiocarbon Database (CARD)<br>- Oxford Radiocarbon Accelerator Unit (ORAU)<br>- CBA Radiocarbon Index (UK & Ireland)<br>- NOSAMS Public Radiocarbon Datasets<br>- IntCal/INTIMATE Database<br>- Radiocarbon Palaeoclimate Database (Reimer et al.)<br>- R_Combine (European compilation)<br>- Open Context Radiocarbon datasets<br>- XRONOS.ch (Swiss Radiocarbon & Archaeological contexts)</div> |

---

## Features | <div dir="rtl">الميزات</div>

| English | <div dir="rtl">Arabic</div> |
|---|---|
| The `data-explorer.html` includes the following features: | <div dir="rtl">يشتمل `data-explorer.html` على الميزات التالية:</div> |
| - **Interactive Map**: Utilizes Leaflet.js to display the radiocarbon records on an Esri Satellite base map.<br>- **Marker Clustering**: Automatically groups nearby data points into clusters for better visualization.<br>- **Detailed Popups**: Clicking on a data point reveals detailed information, including site name, age, lab code, material, and source.<br>- **Advanced Filtering**: Allows users to filter data by age range, material type, and source database.<br>- **Data Summary**: Provides a summary of the total number of samples and sites.<br>- **Responsive Design**: Ensures a seamless experience on both desktop and mobile devices. | <div dir="rtl">- **خريطة تفاعلية**: تستخدم Leaflet.js لعرض سجلات الكربون المشع على خريطة أساس Esri Satellite.<br>- **تجميع العلامات**: يقوم تلقائيًا بتجميع نقاط البيانات القريبة في مجموعات لتصور أفضل.<br>- **نوافذ منبثقة مفصلة**: يكشف النقر على نقطة بيانات عن معلومات مفصلة، بما في ذلك اسم الموقع والعمر ورمز المختبر والمادة والمصدر.<br>- **تصفية متقدمة**: تتيح للمستخدمين تصفية البيانات حسب نطاق العمر ونوع المادة وقاعدة بيانات المصدر.<br>- **ملخص البيانات**: يقدم ملخصًا لإجمالي عدد العينات والمواقع.<br>- **تصميم متجاوب**: يضمن تجربة سلسة على كل من أجهزة سطح المكتب والأجهزة المحمولة.</div> |

---

## Technical Stack | <div dir="rtl">التقنيات المستخدمة</div>

| English | <div dir="rtl">Arabic</div> |
|---|---|
| - **HTML5**: For the structure of the data explorer.<br>- **CSS3**: For styling the user interface with an academic color palette.<br>- **JavaScript (ES6)**: For the core logic and interactivity.<br>- **Leaflet.js**: For the interactive map functionality.<br>- **D3.js (optional)**: For advanced data visualization.<br>- **Turf.js (optional)**: For geospatial analysis. | <div dir="rtl">- **HTML5**: لهيكل مستكشف البيانات.<br>- **CSS3**: لتصميم واجهة المستخدم باستخدام لوحة ألوان أكاديمية.<br>- **JavaScript (ES6)**: للمنطق الأساسي والتفاعلية.<br>- **Leaflet.js**: لوظيفة الخريطة التفاعلية.<br>- **D3.js (اختياري)**: لتصور البيانات المتقدم.<br>- **Turf.js (اختياري)**: للتحليل الجغرافي المكاني.</div> |

---

## Usage | <div dir="rtl">الاستخدام</div>

| English | <div dir="rtl">Arabic</div> |
|---|---|
| To use the data explorer, simply open the `data-explorer.html` file in your web browser. The application will load the `Morocco_c14_data.geojson` file and display the data on the interactive map. You can then use the filtering options and map controls to explore the dataset. | <div dir="rtl">لاستخدام مستكشف البيانات، ما عليك سوى فتح ملف `data-explorer.html` في متصفح الويب الخاص بك. سيقوم التطبيق بتحميل ملف `Morocco_c14_data.geojson` وعرض البيانات على الخريطة التفاعلية. يمكنك بعد ذلك استخدام خيارات التصفية وعناصر التحكم في الخريطة لاستكشاف مجموعة البيانات.</div> |

---

## License | <div dir="rtl">الرخصة</div>

| English | <div dir="rtl">Arabic</div> |
|---|---|
| This project is licensed under the MIT License. See the `LICENSE` file for more details. | <div dir="rtl">هذا المشروع مرخص بموجب رخصة MIT. انظر ملف `LICENSE` لمزيد من التفاصيل.</div> |
