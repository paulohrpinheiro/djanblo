"""Tests for inexistent post path."""

from django.test import TestCase, RequestFactory

from api import views

from util import json


class ApiInexistentPostTests(TestCase):
    """Test api posts resource for inexistent post."""

    @classmethod
    def setUpClass(cls):
        """Setup ApiInexistentPostTests tests."""
        super(ApiInexistentPostTests, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.request = cls.factory.get('/posts')
        cls.response = views.get_post(cls.request, path='inexistent')
        cls.json_response = json.to_json(cls.response.content)

    def test_inexistent_post_status(self):
        """Test status for inexistent post."""
        self.assertEqual('fail', self.json_response['status'])

    def test_inexistent_post_message(self):
        """Test message for inexistent post."""
        self.assertIn('not exist', self.json_response['message'])

    def test_inexistent_post_http_status_code(self):
        """Test HTTP status code for inexistent post."""
        self.assertEqual(self.response.status_code, 404)
