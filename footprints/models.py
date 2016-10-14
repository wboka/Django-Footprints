from django.db import models

class Footprint(models.Model):
	date_accessed = models.DateTimeField(auto_now=True, editable=False)
	ip = models.GenericIPAddressField(editable=False)
	method = models.CharField(max_length=25, editable=False)
	path = models.CharField(max_length=1000, editable=False)
	scheme = models.CharField(max_length=25, editable=False)
	username = models.CharField(max_length=150, editable=False)

	def __str__(self):
		return '[' + str(self.date_accessed) + '] ' + self.path + ' by ' + self.username
