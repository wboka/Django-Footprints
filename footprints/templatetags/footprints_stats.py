from django import template
from .models import Footprint

register = template.Library()

@register.simple_tag
def get_hits(page):
    all_hits = Footprint.objects.all()
    filtered_hits = all_hits.filter(path=page)
    
    return '{0} / {1}'.format(filtered_hits.count(), all_hits.count()
