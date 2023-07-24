from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.trip.models.destiny_model import Destiny
from apps.trip.serializer.destiny_serializer import DestinySerializer


class TestDestinySerializer(APITestCase):

    def setUp(self):
        self.list_url = reverse('destiny-list')

        self.destiny_1 = Destiny.objects.create(
            photo='destiny_photos/germany.jpg',
            name='Germany',
            price=1000.00
        )
        self.destiny_2 = Destiny.objects.create(
            photo='destiny_photos/italy.jpg',
            name='Italy',
            price=2000.00
        )

    def test_destiny_should_have_serialized_fields(self):
        serializer = DestinySerializer(self.destiny_1)
        data = serializer.data

        self.assertEqual(set(data.keys()), {'id', 'photo', 'name', 'price', 'created_at'})

    def test_should_serialize_destiny_data(self):
        serializer = DestinySerializer(self.destiny_1)
        data = serializer.data

        self.assertIsNotNone(data['id'], self.destiny_1.id)
        self.assertEqual(data['name'], self.destiny_1.name)
        self.assertEqual(data['price'], f'{self.destiny_1.price:.2f}')
        self.assertIsNotNone(data['photo'])
        self.assertIsNotNone(data['created_at'])

    def test_should_list_all_destinies(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_should_retrieve_destiny_by_id(self):
        response = self.client.get(reverse('destiny-detail', kwargs={'pk': self.destiny_1.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.destiny_1.name)
        self.assertEqual(response.data['price'], f'{self.destiny_1.price:.2f}')
        self.assertIsNotNone(response.data['photo'])
        self.assertIsNotNone(response.data['created_at'])

    def test_should_create_destiny(self):
        data = {
            'photo': '',
            'name': 'Brazil',
            'price': 500.00
        }
        response = self.client.post(self.list_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['price'], f'{data["price"]:.2f}')
        self.assertIsNotNone(response.data['created_at'])

    def test_should_update_destiny(self):
        data = {
            'photo': '',
            'name': 'Paris',
            'price': 1500.00
        }
        response = self.client.put(reverse('destiny-detail', kwargs={'pk': self.destiny_1.pk}), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['price'], f'{data["price"]:.2f}')
        self.assertIsNotNone(response.data['created_at'])

    def test_should_delete_destiny(self):
        response = self.client.delete(reverse('destiny-detail', kwargs={'pk': self.destiny_1.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Destiny.objects.count(), 1)

    def test_should_search_destiny_by_name(self):
        response = self.client.get(self.list_url, data={'search': 'Germany'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.destiny_1.name)
        self.assertEqual(response.data[0]['price'], f'{self.destiny_1.price:.2f}')
        self.assertIsNotNone(response.data[0]['photo'])
        self.assertIsNotNone(response.data[0]['created_at'])
