from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.trip.models.statement_model import Statement
from apps.trip.serializer.statement_serializer import StatementSerializer


class TestStatementSerializer(APITestCase):

    def setUp(self):
        self.list_url = reverse('statement-list')

        self.statement_1 = Statement.objects.create(
            photo='statement_photos/germany.jpg',
            text='Germany is a country in Western Europe.',
            person='John Doe'
        )
        self.statement_2 = Statement.objects.create(
            photo='statement_photos/italy.jpg',
            text='Italy is a country in Southern Europe.',
            person='Jane Doe'
        )
        self.statement_3 = Statement.objects.create(
            photo='statement_photos/france.jpg',
            text='France is a country in Western Europe.',
            person='John Doe'
        )

    def test_statement_should_have_serialized_fields(self):
        serializer = StatementSerializer(self.statement_1)
        data = serializer.data

        self.assertEqual(set(data.keys()), {'id', 'photo', 'text', 'person', 'created_at'})

    def test_should_serialize_statement_data(self):
        serializer = StatementSerializer(self.statement_1)
        data = serializer.data

        self.assertIsNotNone(data['id'], self.statement_1.id)
        self.assertEqual(data['text'], self.statement_1.text)
        self.assertEqual(data['person'], self.statement_1.person)
        self.assertIsNotNone(data['photo'])
        self.assertIsNotNone(data['created_at'])

    def test_should_list_all_statements(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_should_retrieve_statement_by_id(self):
        response = self.client.get(reverse('statement-detail', kwargs={'pk': self.statement_1.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], self.statement_1.text)
        self.assertEqual(response.data['person'], self.statement_1.person)
        self.assertIsNotNone(response.data['photo'])
        self.assertIsNotNone(response.data['created_at'])

    def test_should_create_statement(self):
        data = {
            'photo': '',
            'text': 'Brazil is a country in South America.',
            'person': 'John Doe'
        }

        response = self.client.post(self.list_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['text'], data['text'])
        self.assertEqual(response.data['person'], data['person'])
        self.assertIsNotNone(response.data['created_at'])

    def test_should_update_statement(self):
        data = {
            'photo': '',
            'text': 'Brazil is a country in South America.',
            'person': 'John Doe'
        }

        response = self.client.put(reverse('statement-detail', kwargs={'pk': self.statement_1.pk}), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], data['text'])
        self.assertEqual(response.data['person'], data['person'])
        self.assertIsNotNone(response.data['created_at'])

    def test_should_delete_statement(self):
        response = self.client.delete(reverse('statement-detail', kwargs={'pk': self.statement_1.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_should_get_first_3_statements(self):
        response = self.client.get(reverse('statement-list-home'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
