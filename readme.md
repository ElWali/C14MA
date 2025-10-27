<a name="readme-top"></a>
# C14MA: A Curated Radiocarbon Database for Morocco

<p align="center">
  <a href="https://github.com/ElWali/C14MA">
    <img src="https://via.placeholder.com/200x200.png?text=C14MA+Logo" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">C14MA</h3>

  <p align="center">
    A Curated Radiocarbon Database for Morocco
    <br />
    <a href="https://github.com/ElWali/C14MA"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ElWali/C14MA">View Demo</a>
    ·
    <a href="https://github.com/ElWali/C14MA/issues">Report Bug</a>
    ·
    <a href="https://github.com/ElWali/C14MA/issues">Request Feature</a>
  </p>
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

---

## Table of Contents

* [About the Project](#about-the-project)
* [Final Deliverables](#final-deliverables)
* [Data Sources](#data-sources)
* [Features](#features)
* [Technical Stack](#technical-stack)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgments](#acknowledgments)

---

## About the Project

| English | <div dir="rtl">Arabic</div> |
|---|---|
| C14MA is a specialized open-source project dedicated to creating a comprehensive and curated GeoJSON database of all known radiocarbon (¹⁴C) records within Morocco. The project aggregates data from the world's top 10 radiocarbon databases, standardizes the information, and presents it through a user-friendly, interactive data explorer. This initiative aims to provide researchers, archaeologists, and historians with a reliable and accessible tool for analyzing chronological data in the region. | <div dir="rtl">C14MA هو مشروع متخصص مفتوح المصدر يهدف إلى إنشاء قاعدة بيانات GeoJSON شاملة ومنسقة لجميع سجلات الكربون المشع (¹⁴C) المعروفة داخل المغرب. يقوم المشروع بتجميع البيانات من أكبر 10 قواعد بيانات للكربون المشع في العالم، وتوحيد المعلومات، وتقديمها من خلال مستكشف بيانات تفاعلي وسهل الاستخدام. تهدف هذه المبادرة إلى تزويد الباحثين وعلماء الآثار والمؤرخين بأداة موثوقة وسهلة الوصول لتحليل البيانات الزمنية في المنطقة.</div> |
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Final Deliverables

| English | <div dir="rtl">Arabic</div> |
|---|---|
| The project will result in two main files: <br> 1. **`Morocco_c14_data.geojson`**: A standardized GeoJSON file containing all the collected radiocarbon records from Morocco. <br> 2. **`data-explorer.html`**: A single-page, professional-grade web application for visualizing and interacting with the GeoJSON data. | <div dir="rtl">سينتج عن المشروع ملفان رئيسيان: <br> 1. **`Morocco_c14_data.geojson`**: ملف GeoJSON موحد يحتوي على جميع سجلات الكربون المشع التي تم جمعها من المغرب. <br> 2. **`data-explorer.html`**: تطبيق ويب احترافي من صفحة واحدة لتصور بيانات GeoJSON والتفاعل معها.</div> |
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Data Sources

| English | <div dir="rtl">Arabic</div> |
|---|---|
| The data is collected and aggregated from the following top 10 global radiocarbon databases: | <div dir="rtl">يتم جمع البيانات وتجميعها من أفضل 10 قواعد بيانات عالمية للكربون المشع التالية:</div> |
| - PEOPLE 3000 (p3k14c)<br>- Canadian Archaeological Radiocarbon Database (CARD)<br>- Oxford Radiocarbon Accelerator Unit (ORAU)<br>- CBA Radiocarbon Index (UK & Ireland)<br>- NOSAMS Public Radiocarbon Datasets<br>- IntCal/INTIMATE Database<br>- Radiocarbon Palaeoclimate Database (Reimer et al.)<br>- R_Combine (European compilation)<br>- Open Context Radiocarbon datasets<br>- XRONOS.ch (Swiss Radiocarbon & Archaeological contexts) | <div dir="rtl">- PEOPLE 3000 (p3k14c)<br>- Canadian Archaeological Radiocarbon Database (CARD)<br>- Oxford Radiocarbon Accelerator Unit (ORAU)<br>- CBA Radiocarbon Index (UK & Ireland)<br>- NOSAMS Public Radiocarbon Datasets<br>- IntCal/INTIMATE Database<br>- Radiocarbon Palaeoclimate Database (Reimer et al.)<br>- R_Combine (European compilation)<br>- Open Context Radiocarbon datasets<br>- XRONOS.ch (Swiss Radiocarbon & Archaeological contexts)</div> |
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Features

| English | <div dir="rtl">Arabic</div> |
|---|---|
| The `data-explorer.html` includes the following features: | <div dir="rtl">يشتمل `data-explorer.html` على الميزات التالية:</div> |
| - **Interactive Map**: Utilizes Leaflet.js to display the radiocarbon records on an Esri Satellite base map.<br>- **Marker Clustering**: Automatically groups nearby data points into clusters for better visualization.<br>- **Detailed Popups**: Clicking on a data point reveals detailed information, including site name, age, lab code, material, and source.<br>- **Advanced Filtering**: Allows users to filter data by age range, material type, and source database.<br>- **Data Summary**: Provides a summary of the total number of samples and sites.<br>- **Responsive Design**: Ensures a seamless experience on both desktop and mobile devices. | <div dir="rtl">- **خريطة تفاعلية**: تستخدم Leaflet.js لعرض سجلات الكربون المشع على خريطة أساس Esri Satellite.<br>- **تجميع العلامات**: يقوم تلقائيًا بتجميع نقاط البيانات القريبة في مجموعات لتصور أفضل.<br>- **نوافذ منبثقة مفصلة**: يكشف النقر على نقطة بيانات عن معلومات مفصلة، بما في ذلك اسم الموقع والعمر ورمز المختبر والمادة والمصدر.<br>- **تصفية متقدمة**: تتيح للمستخدمين تصفية البيانات حسب نطاق العمر ونوع المادة وقاعدة بيانات المصدر.<br>- **ملخص البيانات**: يقدم ملخصًا لإجمالي عدد العينات والمواقع.<br>- **تصميم متجاوب**: يضمن تجربة سلسة على كل من أجهزة سطح المكتب والأجهزة المحمولة.</div> |
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Technical Stack

| English | <div dir="rtl">Arabic</div> |
|---|---|
| - **HTML5**: For the structure of the data explorer.<br>- **CSS3**: For styling the user interface with an academic color palette.<br>- **JavaScript (ES6)**: For the core logic and interactivity.<br>- **Leaflet.js**: For the interactive map functionality.<br>- **D3.js (optional)**: For advanced data visualization.<br>- **Turf.js (optional)**: For geospatial analysis. | <div dir="rtl">- **HTML5**: لهيكل مستكشف البيانات.<br>- **CSS3**: لتصميم واجهة المستخدم باستخدام لوحة ألوان أكاديمية.<br>- **JavaScript (ES6)**: للمنطق الأساسي والتفاعلية.<br>- **Leaflet.js**: لوظيفة الخريطة التفاعلية.<br>- **D3.js (اختياري)**: لتصور البيانات المتقدم.<br>- **Turf.js (اختياري)**: للتحليل الجغرافي المكاني.</div> |
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Roadmap

| English | <div dir="rtl">Arabic</div> |
|---|---|
| - [x] Initial release<br>- [ ] Add more data sources<br>- [ ] Enhance filtering options<br>- [ ] Add a timeline feature | <div dir="rtl">- [x] الإصدار الأولي<br>- [ ] إضافة المزيد من مصادر البيانات<br>- [ ] تحسين خيارات التصفية<br>- [ ] إضافة ميزة الخط الزمني</div> |
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

| English | <div dir="rtl">Arabic</div> |
|---|---|
| Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. <br> 1. Fork the Project<br> 2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)<br> 3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)<br> 4. Push to the Branch (`git push origin feature/AmazingFeature`)<br> 5. Open a Pull Request | <div dir="rtl">المساهمات هي ما تجعل مجتمع المصادر المفتوحة مكانًا رائعًا للتعلم والإلهام والإبداع. أي مساهمات تقدمها هي **موضع تقدير كبير**. <br> 1. قم بعمل Fork للمشروع<br> 2. قم بإنشاء فرع الميزة الخاص بك (`git checkout -b feature/AmazingFeature`)<br> 3. قم بتنفيذ تغييراتك (`git commit -m 'Add some AmazingFeature'`)<br> 4. قم بالدفع إلى الفرع (`git push origin feature/AmazingFeature`)<br> 5. افتح طلب سحب</div> |
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

| English | <div dir="rtl">Arabic</div> |
|---|---|
| Distributed under the MIT License. See `LICENSE` for more information. | <div dir="rtl">موزع بموجب رخصة MIT. انظر `LICENSE` لمزيد من المعلومات.</div> |
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contact

Project Coordinator - [@ProjectCoordinator](https://twitter.com/ProjectCoordinator) - contact@example.com

Project Link: [https://github.com/ElWali/C14MA](https://github.com/ElWali/C14MA)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Acknowledgments

| English | <div dir="rtl">Arabic</div> |
|---|---|
| - [Shields.io](https://shields.io/)<br>- [Font Awesome](https://fontawesome.com)<br>- [Leaflet](https://leafletjs.com/) | <div dir="rtl">- [Shields.io](https://shields.io/)<br>- [Font Awesome](https://fontawesome.com)<br>- [Leaflet](https://leafletjs.com/)</div> |
<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/ElWali/C14MA.svg?style=for-the-badge
[contributors-url]: https://github.com/ElWali/C14MA/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ElWali/C14MA.svg?style=for-the-badge
[forks-url]: https://github.com/ElWali/C14MA/network/members
[stars-shield]: https://img.shields.io/github/stars/ElWali/C14MA.svg?style=for-the-badge
[stars-url]: https://github.com/ElWali/C14MA/stargazers
[issues-shield]: https://img.shields.io/github/issues/ElWali/C14MA.svg?style=for-the-badge
[issues-url]: https://github.com/ElWali/C14MA/issues
[license-shield]: https://img.shields.io/github/license/ElWali/C14MA.svg?style=for-the-badge
[license-url]: https://github.com/ElWali/C14MA/blob/master/LICENSE
