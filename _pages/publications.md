---
title: Publications
layout: publications
permalink: /publications/
description: Publications in reverse chronological order. 
years: [2024, 2023, 2022, 2021, 2020]
nav: true
---
<!-- _pages/publications.md -->

## Publications

<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>

For publications prior to 2020, see [DBLP](https://dblp.org/pid/144/5582.html). 
