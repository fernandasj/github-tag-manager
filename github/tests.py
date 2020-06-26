from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient 

from github import models as exams

class RepositoryTest(TestCase):

    def test_create_test(self):

        user = User.objects.create_user('ada', 'ada@lovelace.com', 'adapassword')
        url = reverse('github-api:api-github-list')

        data = {"name": "django-girls-tutorial", "description":"Implementando um blog com Django", "user": user.pk}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 