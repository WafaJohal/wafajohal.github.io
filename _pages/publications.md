---
layout: page
permalink: /publications/
title: Publications
nav: true
nav_order: 2
years: [2024, 2023, 2022, 2021, 2020]
---
<!-- _pages/publications.md -->


<div class="publications">

{%- for y in page.years %}
  <!-- <h2 class="year">{{y}}</h2> -->
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>

For publications prior to 2020, see [DBLP](https://dblp.org/pid/144/5582.html). 
