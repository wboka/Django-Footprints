from django import template
from .models import Footprint

register = template.Library()

@register.simple_tag
def get_all_hits():
	all_hits = Footprint.objects.all()

	return all_hits.count()

@register.simple_tag
def get_page_hits(page):
    filtered_hits = Footprint.objects.filter(path=page)

    return filtered_hits.count()
