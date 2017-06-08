from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Samuel Barbosa',
            cpf =' 12345678901',
            email = 'contato@smkbarbosa.eti.br',
            phone = '63-98137-3175'
        )

        self.obj.save()

    def test_create(self):

        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Samuel Barbosa', str(self.obj))