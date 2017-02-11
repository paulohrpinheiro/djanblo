from django.test import TestCase, RequestFactory
from django.conf import settings

from util.fixtures import generate

from blog.views import index


class PostIndexViewTest(TestCase):
    """Test index post view"""

    @classmethod
    def setUpClass(cls):
        """Create fake data for tests"""
         # http://stackoverflow.com/questions/29653129/update-to-django-1-8-attributeerror-django-test-testcase-has-no-attribute-cl
        super(PostIndexViewTest, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.pages = 3
        cls.total_posts = (settings.MAX_POSTS_PER_PAGE * (cls.pages - 1)) + 1
        generate(total_authors=5, total_posts=cls.total_posts)
        cls.request = cls.factory.get('/')
        cls.response = index(cls.request)

    def test_response_code(self):
        """Test the number of pages"""
        self.assertEqual(self.response.status_code, 200)
