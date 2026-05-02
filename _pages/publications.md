---
layout: page
permalink: /publications/
title: Publications
nav: false
nav_order: 2
years: [2026, 2025, 2024, 2023, 2022, 2021, 2020]
---

<div class="pv2-pub-page">

<div class="page-header-v2">
  <h1>Publications</h1>
  <p>Peer-reviewed papers in human-robot interaction, learning from demonstration, social robotics, and haptics.<br>
  <em>Wafa Johal</em> is highlighted in each author list.</p>
</div>

<div class="publications">
{%- for y in page.years %}
  <h2 class="year">{{ y }}</h2>
  {% bibliography -f papers -q @*[year={{ y }}]* %}
{% endfor %}
</div>

<p style="margin-top: 32px; font-size: 13px; color: var(--pv2-muted);">
  For earlier publications see <a href="https://dblp.org/pid/144/5582.html" target="_blank" rel="noopener noreferrer">DBLP</a> or <a href="https://scholar.google.com/citations?user=ZbWcKUoAAAAJ" target="_blank" rel="noopener noreferrer">Google Scholar</a>.
</p>

</div>
