"""
Tests for internal error condition.
"""

from django.test import TestCase, RequestFactory

from api import views

from blog.models import Post

from util import json


class ApiListingPostInternalErrorTests(TestCase):
    """Test api posts resource fo listing posts with internal error."""

    @classmethod
    def setUpClass(cls):
        super(ApiListingPostInternalErrorTests, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.table_name = Post._meta.db_table
        Post._meta.db_table = "--{}--".format(cls.table_name)

    @classmethod
    def tearDownClass(cls):
        Post._meta.db_table = cls.table_name

    def test_entrypoint_crash(self):
        """Test result from a requisition in database crash."""
        request = self.factory.get('/')
        response = views.index(request)
        json_response = json.to_json(response.content)
        print(json_response)
        self.assertEqual('success', json_response['status'])
        self.assertEqual(200, response.status_code)

    def test_posts_crash(self):
        """Test result from a requisition in database crash."""
        request = self.factory.get('/posts')
        response = views.get_post(request, path='inexistent')
        json_response = json.to_json(response.content)
        print(json_response)
        self.assertEqual('fail', json_response['status'])
        self.assertEqual(503, response.status_code)
