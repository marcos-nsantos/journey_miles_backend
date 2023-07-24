from django.test import TestCase

from apps.trip.models.destiny_model import Destiny


class TestDestinyModel(TestCase):

    def setUp(self):
        self.destiny = Destiny(
            photo='destiny_photos/germany.jpg',
            name='Germany',
            price=1000.00
        )
        self.destiny.save()

    def test_destiny_model_should_have_attributes(self):
        self.assertEqual(self.destiny.photo, 'destiny_photos/germany.jpg')
        self.assertEqual(self.destiny.name, 'Germany')
        self.assertEqual(self.destiny.price, 1000.00)
        self.assertIsNotNone(self.destiny.created_at)
