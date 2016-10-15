from django.test import TestCase
from .models import Footprint

class FootprintTestCase(TestCase):
	def setUp(self):
		Footprint.objects.create(ip='0.0.0.0', method='GET', scheme='http', path='/', username='AnonymousUser')

	def test_footprints_left(self):
		footprints = Footprint.objects.all()

		self.assertGreater(footprints.count(), 0)
		self.assertEqual(footprints.count(), 1)
		self.assertNotEqual(footprints.count(), 0)
		self.assertNotEqual(footprints.count(), 2)
		self.assertNotEqual(footprints.count(), 3)
		self.assertNotEqual(footprints.count(), 4)
