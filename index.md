---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: Etiquetas / Labels
---

<div class="intro">
  <div class="intro-text">
    <p>Información de salud y seguridad de 40 etiquetas de pesticidas muy utilizados en huertas de manzano y peral de Washington.</p>
    <h3>Estas traducciones son solo para información. La etiqueta es la ley.</h3>

    <p><hr /></p>


    <p>Health and Safety information from 40 top labels used in Washington State apple and pear orchards.</p>
    <h3>These translations are for information only. The label is the law.</h3>
  </div>

  <div class="sponsor-logos">
    <a href="https://deohs.washington.edu/pnash/" target="_blank"><img src="{{ "/img/PNASH-logo-web-150ppi-sq.png" | relative_url }}" alt="PNASH" /></a>
    <a href="https://www.washington.edu/" target="_blank"><img src="{{ "/img/W-Logo_Purple_Hex_sq.png" | relative_url }}" alt="UW" /></a>
    <a href="https://lni.wa.gov/safety-health/grants-committees-partnerships/safety-health-investment-projects-grant-program/" target="_blank"><img src="{{ "/img/SHIP Grant funded by L_I.svg" | relative_url }}" alt="SHIP Grant" /></a>
  </div>
</div>

{% assign labels = site.label_pages | sort_natural: "title" %}
{% for label in labels %}
  <h3><a href="{{ label.url | relative_url }}">{{ label.title }}</a></h3>
{% endfor %}

<div>
  Spanish translations/Traducciones al español <img src="{{ "/img/52px-Cc.logo.circle.png" | relative_url }}" alt="CC" class="cc-mark" /> BY-NC-SA 4.0 The State of Washington 2020 – 2022
</div>
