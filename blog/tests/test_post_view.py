"""Tests for post app views."""

from django.test import TestCase, RequestFactory
from django.conf import settings
from django.http.response import Http404
from django.contrib.auth.models import User

from util.fixtures import generate

from blog import views

from blog.models import Post

from bs4 import BeautifulSoup


class PostIndexPaginationTest(TestCase):
    """Test index post view"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = None
        self.response = None
        self.soup = None
        self.pagination = None

    @classmethod
    def setUpClass(cls):
        """Create fake data for tests"""
        # https://goo.gl/O9c9g0
        super(PostIndexPaginationTest, cls).setUpClass()

        cls.factory = RequestFactory()
        cls.total_posts = ((settings.MAX_POSTS_PER_PAGE * 3) - 1)
        generate(total_authors=5, total_posts=cls.total_posts)

    def get_page(self, number=0):
        """Get the specified page, or first page withoutr parameter"""
        if number == 0:
            self.request = self.factory.get('/')
        else:
            self.request = self.factory.get('/?page={}'.format(number))

        self.response = views.index(self.request)

        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        self.pagination = self.soup.find_all('ul', class_='pagination')

    def test_ordered(self):
        """Test if posts are date sorted"""
        dt_list = []
        # pages begins in 1, but 0 is a special value for get_page()
        for page_number in [0, 2, 3]:
            self.get_page(page_number)
            date = self.soup.find(class_='post-date')
            while date is not None:
                dt_list.append(date.text)
                date = date.find_next(class_='post-date')

        self.assertTrue(
            all(dt_list[i] >= dt_list[i+1] for i in range(len(dt_list)-1))
        )

    def test_response_code_first_page(self):
        """Test response code in first page"""
        self.get_page()
        self.assertEqual(self.response.status_code, 200)

    def test_response_code_inexistent_page(self):
        """Test if return a valid page for a invalid page number"""
        self.get_page(int(1e10))
        self.assertEqual(self.response.status_code, 200)

    def test_response_code_string_page(self):
        """Test if return a valid page for a string page number"""
        self.get_page('this is not a number!')
        self.assertEqual(self.response.status_code, 200)

    def test_has_pagination_first_page(self):
        """Test if first page has pagination class in html"""
        self.get_page()
        self.assertEqual(len(self.pagination), 1)

    def test_pagination_has_first_in_first_page(self):
        """Test if first page has the 'first' link in pagination"""
        self.get_page()
        self.assertNotIn('First', self.pagination[0].text)

    def test_response_code_second_page(self):
        """Test response code in second page"""
        self.get_page(2)
        self.assertEqual(self.response.status_code, 200)

    def test_has_pagination_second_page(self):
        """Test if second page has pagination class in html"""
        self.get_page(2)
        self.assertEqual(len(self.pagination), 1)

    def test_response_code_last_page(self):
        """Test response code in last page"""
        self.get_page(3)
        self.assertEqual(self.response.status_code, 200)

    def test_has_pagination_last_page(self):
        """Test if last page has pagination class in html"""
        self.get_page(3)
        self.assertEqual(len(self.pagination), 1)

    def test_pagination_has_last_in_last_page(self):
        """Test if last page has the 'last' link in pagination"""
        self.get_page(3)
        self.assertNotIn('Last', self.pagination[0].text)


class PostPostTest(TestCase):
    """Test post post view"""

    def setUp(self):
        """Create factory"""
        self.factory = RequestFactory()

    def tearDown(self):
        """Destroy data in database"""
        Post.objects.all().delete()
        User.objects.all().delete()

    def test_get_existent_page(self):
        """Test response code for an existent post"""
        generate(total_authors=1, total_posts=1)
        post = Post.objects.first()
        request = self.factory.get('/post')
        response = views.post(request, path=post.path)
        self.assertEqual(response.status_code, 200)

    def test_get_inexistent_page(self):
        """Test response code for an inexistent post"""
        request = self.factory.get('/post')
        self.assertRaises(Http404, views.post, request, path='non exist')
