from django.test import TestCase, RequestFactory
from unittest import skip

from api import views

from blog.models import Post

from util import json


class ApiListingPostInternalErrorTests(TestCase):
    """Test api posts resource fo listing posts with internal error."""

    @skip('Think in a better way for a crash.')
    @classmethod
    def setUpClass(cls):
        super(ApiListingPostInternalErrorTests, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.table_name = Post._meta.db_table
        Post._meta.db_table = "--{}--".format(cls.table_name)

    @skip('Think in a better way for a crash.')
    def tearDownClass(cls):
        Post._meta.db_table = cls.table_name

    @skip('Think in a better way for a crash.')
    def test_entrypoint_crash(self):
        """Test result from a requisition in database crash."""
        request = self.factory.get('/posts')
        response = views.index(request)
        json_response = json.to_json(response.content)
        self.assertEqual('failed', json_response['status'])
        self.assertEqual(404, response.status_code)
