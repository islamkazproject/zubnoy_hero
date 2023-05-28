from django.test import TestCase

from zubnoy_app.models import Presentation
from zubnoy_app.serializers import UserSerializer


class PresentationSerializerTestCase(TestCase):
    def test_ok(self):
        presentation_1 = Presentation.objects.create(title='Test presentation 1', content='Test case 1')
        presentation_2 = Presentation.objects.create(title='Test presentation 2', content='Test case 2')
        data = UserSerializer([presentation_1, presentation_2], many=True).data
        expected_data = [
            {
                'id': presentation_1.id,
                'title': 'Test presentation 1',
                'content': 'Test case 1',
            },
            {
                'id': presentation_2.id,
                'title': 'Test presentation 2',
                'content': 'Test case 2',
            },
        ]
        self.assertEqual(expected_data, data)
