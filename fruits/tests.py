from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Fruit

class FruitTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='test', password='1234')
        testuser1.save()

        test_fruit = Fruit.objects.create(name='Apple', owner=testuser1,flavor='Sweet/Tart')
        test_fruit.save()

    def test_fruits_model(self):
        fruit = Fruit.objects.get(id=1)
        actual_owner = str(fruit.owner)
        actual_name = str(fruit.name)
        actual_flavor = str(fruit.flavor)
        self.assertEqual(actual_owner,'test')
        self.assertEqual(actual_name, 'Apple')
        self.assertEqual(actual_flavor,'Sweet/Tart')