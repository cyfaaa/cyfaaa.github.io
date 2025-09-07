---
layout: archive
title: "Projects"
permalink: /Projects/
author_profile: true
entries_layout: grid
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.projects reversed %}
  {% include archive-single.html type="grid" %}
{% endfor %}
