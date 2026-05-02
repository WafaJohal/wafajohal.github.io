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
  <p>Courses taught at the University of Melbourne and previously at EPFL. I supervise PhD and Honours students working on human-robot interaction, robot learning, and social robotics.</p>
</div>

{% for institution in site.data.teaching.institutions %}
<div class="pv2-sec-title">{{ institution.name }}</div>
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

<div class="pv2-sec-title">Current PhD Students</div>
<div class="students-grid">
  {% for student in site.data.students.current %}
  <div class="student-card">
    <div class="student-name">{{ student.name }}</div>
    <div class="student-level">{{ student.level }}</div>
    <div class="student-topic">{{ student.topic }}</div>
    <div class="student-cohort">Enrolled {{ student.enrolled }} · {{ student.institution }}</div>
  </div>
  {% endfor %}
</div>

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
