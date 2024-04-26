---
layout: gridlay
title: "Research"
permalink: /research/
author_profile: true
---

<h1> A test </h1>

{% for post in site.portfolio %}

{% if post.highlight == 1 %}

<p>{{ post.title  }}</p>

<div class="row">


<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ post.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}{{ post.photo }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ post.description }}</p>
 </div>
</div>

{% endif %}

{% endfor %}

</div>

