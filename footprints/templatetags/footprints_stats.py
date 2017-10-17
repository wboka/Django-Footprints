from django import template
from .models import Footprint

register = template.Library()

@register.simple_tag
def get_hits(page):
    footprints_by_path = Footprint.objects.filter(path=page)
    
    return footprints_by_path.count()
