from django import template
from django.contrib.staticfiles import finders
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def inline_svg(path):
    absolute_path = finders.find(path)
    if absolute_path:
        with open(absolute_path, 'r', encoding='utf-8') as f:
            svg_content = f.read()
        return mark_safe(svg_content)
    return mark_safe(f'<!-- SVG file not found: {path} -->')