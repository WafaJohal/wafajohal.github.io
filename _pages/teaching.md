---
layout: page
permalink: /teaching/
title: Teaching
nav: true
nav_order: 4
---

<div class="pv2-teaching-page">

<div class="page-header-v2">
  <h1>Teaching</h1>
  <p>Courses taught at the University of Melbourne, UNSW, and EPFL. I supervise PhD and MPhil students working on human-robot interaction, robot learning, social robotics, and haptics.</p>
</div>

{% for institution in site.data.teaching.institutions %}
<div class="pv2-sec-title">{{ institution.name }}{% if institution.years %} <span style="font-weight:400;letter-spacing:0">· {{ institution.years }}</span>{% endif %}</div>
<div class="course-block">
  {% for course in institution.courses %}
  <div class="course-row">
    <div class="course-code">{{ course.code }}</div>
    <div class="course-info">
      <div class="course-name">{% if course.url %}<a href="{{ course.url }}" target="_blank" rel="noopener noreferrer">{{ course.title }}</a>{% else %}{{ course.title }}{% endif %}</div>
      <div class="course-meta">{{ course.desc }}</div>
      <span class="course-level {% if course.level == 'undergraduate' %}undergrad{% else %}postgrad{% endif %}">{{ course.level | capitalize }}</span>
    </div>
    <div class="course-term">{{ course.years }}</div>
  </div>
  {% endfor %}
</div>
{% endfor %}

<div class="pv2-sec-title">Current Students</div>
<div class="students-grid">
  {% for student in site.data.students.current %}
  <div class="student-card">
    <div class="student-name">{{ student.name }}{% if student.primary %} <span style="color:var(--pv2-accent);font-size:10px" title="Primary supervisor">★</span>{% endif %}</div>
    <div class="student-level">{{ student.level }}</div>
    <div class="student-topic">{{ student.topic }}</div>
    <div class="student-cohort">{{ student.enrolled }}– · {{ student.institution }}</div>
  </div>
  {% endfor %}
</div>

{% if site.data.students.past and site.data.students.past.size > 0 %}
<div class="pv2-sec-title">Past Students</div>
<div class="students-grid">
  {% for student in site.data.students.past %}
  <div class="student-card" style="opacity:0.8">
    <div class="student-name">{{ student.name }}</div>
    <div class="student-level">{{ student.level }}</div>
    <div class="student-topic">{{ student.topic }}</div>
    <div class="student-cohort">{{ student.years }} · {{ student.institution }}</div>
  </div>
  {% endfor %}
</div>
{% endif %}

<div class="pv2-sec-title">Open Research Topics</div>
<div class="topics-list">
  {% for topic in site.data.teaching.topics %}
  <div class="topic-item">
    <div class="topic-name">{{ topic.name }}</div>
    <span class="topic-badge {% if topic.status == 'open' %}open{% endif %}">{% if topic.status == 'open' %}Open{% else %}Potentially available{% endif %}</span>
  </div>
  {% endfor %}
</div>

</div>
