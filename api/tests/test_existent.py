"""Tests for existent post."""

from django.test import TestCase, RequestFactory

from api import views

from blog.models import Post

from util import fixtures, json


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
        cls.json_response = json.to_json(cls.response.content)

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
        fields = 'publication_date path title subject content author link ref'\
            .split()
        self.assertEqual(set(fields), set(self.json_response['post']))
