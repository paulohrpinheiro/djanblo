from django.test import TestCase, RequestFactory

from api import views

from blog.models import Post

from util import fixtures

import json


class ApiEntryPointTest(TestCase):
    """Test api entry point"""

    def setUp(self):
        """Setup ApiEntryPointTest tests."""
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        self.response = views.index(self.request)
        # Only python >= 3.6 accept str & bytes in json.loads
        self.json_response = json.loads(str(self.response.content, 'utf-8'))

    def test_response_have_all_fields(self):
        """Test if entry point give a response with all fields"""
        expected = 'status message post_content posts_listing'.split()
        self.assertEqual(set(expected), set(self.json_response.keys()))

    def test_response_status(self):
        """Test if entry point returns a success status"""
        self.assertEqual('success', self.json_response['status'])


class ApiInexistentPostTests(TestCase):
    """Test api posts resource for inexistent post."""

    @classmethod
    def setUpClass(cls):
        """Setup ApiInexistentPostTests tests."""
        super(ApiInexistentPostTests, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.request = cls.factory.get('/posts')
        cls.response = views.get_post(cls.request, path='inexistent')
        cls.json_response = json.loads(str(cls.response.content, 'utf-8'))

    def test_inexistent_post_status(self):
        """Test status for inexistent post."""
        self.assertEqual('failed', self.json_response['status'])

    def test_inexistent_post_message(self):
        """Test message for inexistent post."""
        self.assertIn('not exist', self.json_response['message'])

    def test_inexistent_post_http_status_code(self):
        """Test HTTP status code for inexistent post."""
        self.assertEqual(self.response.status_code, 404)


class ApiExistentPostTests(TestCase):
    """Test api posts resource for existent post."""

    @classmethod
    def setUpClass(cls):
        """Setup ApiExistentPostTests class tests."""
        super(ApiExistentPostTests, cls).setUpClass()
        fixtures.generate(1, 1)
        cls.post = Post.objects.first()
        cls.factory = RequestFactory()
        cls.request = cls.factory.get('/posts')
        cls.response = views.get_post(cls.request, path=cls.post.path)
        cls.json_response = json.loads(str(cls.response.content, 'utf-8'))

    def setUp(self):
        """Setup ApiExistentPostTests tests."""
        pass

    def test_existent_post_status(self):
        """Test status for existent post."""
        self.assertEqual('success', self.json_response['status'])

    def test_inexistent_post_message(self):
        """Test message for existent post."""
        self.assertEqual('', self.json_response['message'])

    def test_existent_post_http_status_code(self):
        """Test HTTP status code for existent post."""
        self.assertEqual(self.response.status_code, 200)

    def test_existent_post_get_correct_data(self):
        """Test if get all fields from database."""
        fields = 'publication_date path title subject content author link'\
            .split()
        self.assertEqual(set(fields), set(self.json_response['post']))
