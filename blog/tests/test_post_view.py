from django.test import TestCase, RequestFactory
from django.conf import settings

from util.fixtures import generate

from blog.views import index

from bs4 import BeautifulSoup


class PostIndexPaginationTest(TestCase):
    """Test index post view"""

    @classmethod
    def setUpClass(cls):
        """Create fake data for tests"""
        # http://stackoverflow.com/questions/29653129/update-to-django-1-8-attributeerror-django-test-testcase-has-no-attribute-cl
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

        self.response = index(self.request)

        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        self.pagination = self.soup.find_all('div', class_='pagination')

    def test_ordered(self):
        """Test if posts are date sorted"""
        dt = []
        # pages begins in 1, but 0 is a special value for get_page()
        for page_number in [0,2,3]:
            self.get_page(page_number)
            date = self.soup.find(class_='post-date')
            while date is not None:
                dt.append(date.text)
                date = date.find_next(class_='post-date')

        self.assertTrue(all(dt[i] >= dt[i+1] for i in range(len(dt)-1)))

    def test_response_code_first_page(self):
        """Test the number of pages in first page"""
        self.get_page()
        self.assertEqual(self.response.status_code, 200)

    def test_response_code_inexistent_page(self):
        """Test if return a valid page for a invalid page number"""
        self.get_page(int(1e10))
        self.assertEqual(self.response.status_code, 200)

    def test_inexistent_page_get_first_page(self):
        """Test if returns last page when page number is inexistent"""
        self.get_page(int(1e10))
        self.assertIn('Page 3 of 3.', self.pagination[0].text)

    def test_response_code_string_page(self):
        """Test if return a valid page for a string page number"""
        self.get_page('this is not a number!')
        self.assertEqual(self.response.status_code, 200)

    def test_string_page_get_first_page(self):
        """Test if returns last page when page number is a string"""
        self.get_page('this is not a number!')
        self.assertIn('Page 1 of 3.', self.pagination[0].text)

    def test_has_pagination_first_page(self):
        """Test if first page has pagination class in html"""
        self.get_page()
        self.assertEquals(len(self.pagination), 1)

    def test_pagination_has_first_in_first_page(self):
        """Test if first page has the 'first' link in pagination"""
        self.get_page()
        self.assertNotIn('First', self.pagination[0].text)

    def test_pagination_has_last_in_first_page(self):
        """Test if first page has the 'last' link in pagination"""
        self.get_page()
        self.assertIn('Last', self.pagination[0].text)

    def test_pagination_total_pages_first_page(self):
        """Test if display the correct total number of pages in first page"""
        self.get_page()
        self.assertIn('Page 1 of 3.', self.pagination[0].text)

    def test_response_code_second_page(self):
        """Test the number of pages in second page"""
        self.get_page(2)
        self.assertEqual(self.response.status_code, 200)

    def test_has_pagination_second_page(self):
        """Test if second page has pagination class in html"""
        self.get_page(2)
        self.assertEquals(len(self.pagination), 1)

    def test_pagination_has_first_in_second_page(self):
        """Test if second page has the 'first' link in pagination"""
        self.get_page(2)
        self.assertIn('First', self.pagination[0].text)

    def test_pagination_has_last_in_second_page(self):
        """Test if second page has the 'last' link in pagination"""
        self.get_page(2)
        self.assertIn('Last', self.pagination[0].text)

    def test_pagination_total_pages_second_page(self):
        """Test if display the correct total number of pages in second page"""
        self.get_page(2)
        self.assertIn('Page 2 of 3.', self.pagination[0].text)

    def test_response_code_last_page(self):
        """Test the number of pages in last page"""
        self.get_page(3)
        self.assertEqual(self.response.status_code, 200)

    def test_has_pagination_last_page(self):
        """Test if last page has pagination class in html"""
        self.get_page(3)
        self.assertEquals(len(self.pagination), 1)

    def test_pagination_has_first_in_last_page(self):
        """Test if last page has the 'first' link in pagination"""
        self.get_page(3)
        self.assertIn('First', self.pagination[0].text)

    def test_pagination_has_last_in_last_page(self):
        """Test if last page has the 'last' link in pagination"""
        self.get_page(3)
        self.assertNotIn('Last', self.pagination[0].text)

    def test_pagination_total_pages_last_page(self):
        """Test if display the correct total number of pages in last page"""
        self.get_page(3)
        self.assertIn('Page 3 of 3.', self.pagination[0].text)
