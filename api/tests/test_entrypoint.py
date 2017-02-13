from django.test import TestCase, RequestFactory

from api import views

from util import json


class ApiEntryPointTest(TestCase):
    """Test api entry point"""

    def setUp(self):
        """Setup ApiEntryPointTest tests."""
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        self.response = views.index(self.request)
        self.json_response = json.to_json(self.response.content)

    def test_response_have_all_fields(self):
        """Test if entry point give a response with all fields"""
        expected = 'status message post_content posts_listing'.split()
        self.assertEqual(set(expected), set(self.json_response.keys()))

    def test_response_status(self):
        """Test if entry point returns a success status"""
        self.assertEqual('success', self.json_response['status'])
