import unittest.mock as mock

from django.test import TestCase


from .models import get_image_path


class CatagoryTestCase(TestCase):

    def test_get_image_path(self):
        f = 'TestFile.jpg'
        instance = mock.Mock()
        instance.name = 'Somethingelse'
        filename = get_image_path(instance, f)
        self.assertEqual(filename, 'somethingelse.jpg')

        instance.name = 'Something else'
        filename = get_image_path(instance, f)
        self.assertEqual(filename, 'something-else.jpg')
