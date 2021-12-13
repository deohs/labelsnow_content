---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---
{% assign labels = site.label_pages | sort_natural: "title" %}
{% for label in labels %}
  <h3><a href="{{ label.url }}">{{ label.title }}</a></h3>
{% endfor %}