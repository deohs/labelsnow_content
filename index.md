---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<div class="intro">
  <div class="intro-text">
    <p>Información de salud y seguridad de 40 etiquetas de pesticidas muy utilizados en huertas de manzano y peral de Washington. <br />Estas traducciones son solo para información. La etiqueta es la ley.</p>
    <p>Health and Safety information from 40 top labels used in Washington State apple and pear orchards. <br />These translations are for information only. The label is the law.</p>
  </div>

  <div class="sponsor-logos">
    <img src="{{ "/img/PNASH-logo-web-150ppi-sq.png" | relative_url }}" alt="PNASH" />
    <img src="{{ "/img/W-Logo_Purple_Hex_sq.png" | relative_url }}" alt="UW" />
    <img src="{{ "/img/SHIP Grant funded by L_I.svg" | relative_url }}" alt="SHIP Grant" />
  </div>
</div>

{% assign labels = site.label_pages | sort_natural: "title" %}
{% for label in labels %}
  <h3><a href="{{ label.url | relative_url }}">{{ label.title }}</a></h3>
{% endfor %}
