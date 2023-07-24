from django.test import TestCase

from apps.trip.models.statement_model import Statement


class TestStatementModel(TestCase):

    def setUp(self):
        self.statement = Statement(
            photo='statement_photos/germany.jpg',
            text='Germany is a country in Western Europe.',
            person='John Doe'
        )
        self.statement.save()

    def test_statement_model_should_have_attributes(self):
        self.assertEqual(self.statement.photo, 'statement_photos/germany.jpg')
        self.assertEqual(self.statement.text, 'Germany is a country in Western Europe.')
        self.assertEqual(self.statement.person, 'John Doe')
        self.assertIsNotNone(self.statement.created_at)
