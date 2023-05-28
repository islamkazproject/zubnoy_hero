from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from zubnoy_app.models import Presentation
from zubnoy_app.serializers import UserSerializer


class PresentationsApiTestCase(APITestCase):
    def test_get(self):
        presentation_1 = Presentation.objects.create(title='Test presentation 1', content='Test case 1')
        presentation_2 = Presentation.objects.create(title='Test presentation 2', content='Test case 2')
        url = reverse('presentation-list')
        response = self.client.get(url)
        serializer_data = UserSerializer([presentation_1, presentation_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

