from django.contrib import admin
from .models import Footprint

class FootprintAdmin(admin.ModelAdmin):
	readonly_fields = ('date_accessed', 'ip', 'method', 'path', 'scheme', 'username')
	list_display = ('date_accessed', 'path', 'username')
	list_filter = list_display
	list_per_page = 25
	search_fields = list_display

admin.site.register(Footprint, FootprintAdmin)
