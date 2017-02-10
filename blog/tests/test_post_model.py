from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.db import transaction


class PostModelConstrainsTest(TestCase):
    """Test post model and database constrains"""

    @transaction.atomic
    def setUp(self):
        """Create valid user for tests"""
        self.author = User.objects.create_user('auth', 'auth@test.com', 'pass')

    @transaction.atomic
    def tearDown(self):
        """Remove all data"""
        self.author.delete()
        Post.objects.all().delete()

    def create_post(
        self,
        path='/bla',
        title='bla',
        subject='bla',
        content='bla bla bla',
        author=None
    ):
        """Create an instance of Post model"""
        return Post(
            path=path,
            title=title,
            subject=subject,
            content=content,
            author=author
        )

    def test_valid_post(self):
        """Test if accepts an valid post"""
        post = self.create_post(author=self.author)

        try:
            post.full_clean()
        except:
            self.fail('Unexpected full_clean() exception')

        self.assertIsNone(post.save())

    def test_empty_path(self):
        """Test if accepts a blank path field"""
        post = self.create_post(path='', author=self.author)
        self.assertRaisesRegexp(ValidationError, 'path', post.full_clean)
        self.assertFalse(post.save())

    def test_empty_title(self):
        """Test if accepts a blank title field"""
        post = self.create_post(title='', author=self.author)
        self.assertRaisesRegexp(ValidationError, 'title', post.full_clean)
        self.assertFalse(post.save())

    def test_empty_subject(self):
        """Test if accepts a blank subject field"""
        post = self.create_post(subject='', author=self.author)
        self.assertRaisesRegexp(ValidationError, 'subject', post.full_clean)
        self.assertFalse(post.save())

    def test_empty_content(self):
        """Test if accepts a blank content field"""
        post = self.create_post(content='', author=self.author)
        self.assertRaisesRegexp(ValidationError, 'content', post.full_clean)
        self.assertFalse(post.save())

    @transaction.atomic
    def test_invalid_author(self):
        """Test if accepts a invalid author field"""
        post = self.create_post(author=None)
        self.assertRaisesRegexp(ValidationError, 'author', post.full_clean)
        self.assertRaisesRegexp(IntegrityError, 'author', post.save)
