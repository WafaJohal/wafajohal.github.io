---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<div class="projects">
{% for project in site.portfolio %}
    {% if project.link %}
        {% assign proj_url = project.link %}
    {% else %}
        {% capture proj_url %}{{ site.base }}{{ project.url }}{% endcapture %}
    {% endif %}

<div class="col-sm-4 {{ project.area }}">

{% if project.tool %}
<div id="{{ site.base }}{{ project.url }}" class="card card-project {{ project.area }}" style=" cursor: pointer; background-color: {{ project.color }}; color:white;">
{% else %}
<div id="{{ site.base }}{{ project.url }}" class="card card-project {{ project.area }}" style=" cursor: pointer;">
{% endif %}
<a href="{{ proj_url }}">
<img id="project-image" src="{{ site.url }}{{ site.baseurl }}/images/projects/thumbnails/{{ project.image}}" alt="{{project.image.alt-text}}" width="15%" class="img-responsive" style="display:block; margin:auto;" /></a>
<div class="card-body {{ project.area }}">
<p class="title" style="overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 2;
   -webkit-box-orient: vertical;"><a href="{{ proj_url }}" style="color:inherit; text-decoration: none;">{{ project.title }}</a></p>
{% if project.tool %}
<p class="description" style="overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 6;
   -webkit-box-orient: vertical;"><a href="{{ proj_url }}" style="color:white; text-decoration: none;">{{ project.description }}</a></p>
{% else %}
<p class="description" style="overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 6;
   -webkit-box-orient: vertical;"><a href="{{ proj_url }}" style="color:inherit; text-decoration: none;">{{ project.description }}</a></p>
{% endif %}

</div>
</div>
</div>

{% endfor %}
</div>