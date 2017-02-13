from django.test import TestCase, RequestFactory

from api import views

from blog.models import Post

from util import fixtures, json


class ApiListingPostTests(TestCase):
    """Test api posts resource for listing posts."""

    TOTAL_POSTS = 10

    @classmethod
    def setUpClass(cls):
        super(ApiListingPostTests, cls).setUpClass()
        fixtures.generate(total_authors=1, total_posts=cls.TOTAL_POSTS)
        cls.factory = RequestFactory()
        cls.request = cls.factory.get('/posts')
        cls.response = views.list_posts(cls.request)
        cls.json_response = json.to_json(cls.response.content)

    def test_listing_posts_status(self):
        """Test status for listing posts."""
        self.assertEqual('success', self.json_response['status'])

    def test_listing_posts_message(self):
        """Test message for listing posts."""
        self.assertEqual('', self.json_response['message'])

    def test_listing_posts_http_status_code(self):
        """Test HTTP status code for listing posts."""
        self.assertEqual(self.response.status_code, 200)

    def test_listing_posts_correct_post_itens(self):
        """Test if post_count is the quantity of itens in database."""
        self.assertEqual(self.TOTAL_POSTS, self.json_response['posts_count'])
        self.assertEqual(self.TOTAL_POSTS, Post.objects.all().count())
