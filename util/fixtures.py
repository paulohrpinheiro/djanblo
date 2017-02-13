"""Fake data generator for fixtures."""

from random import randrange, choice
from datetime import timezone

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.utils.text import slugify
from django.conf import settings

from faker import Factory

from blog.models import Post


def generate(total_posts, total_authors):
    """Generate and save random data for post and author models."""
    fake = Factory.create(settings.LANGUAGE_CODE)

    authors = []
    created_authors = 0
    while created_authors < total_authors:
        try:
            authors.append(
                User.objects.create_user(
                    fake.user_name(),
                    fake.email(),
                    fake.password(),
                )
            )
            created_authors += 1
        except IntegrityError:
            print("Repeated authors data")

    created_posts = 0
    while created_posts < total_posts:
        try:
            title = fake.sentence(nb_words=6, variable_nb_words=True)
            post = Post.objects.create(
                title=title,
                subject=fake.sentence(nb_words=20, variable_nb_words=True),
                path=slugify(title),
                content='\n'.join(fake.paragraphs(nb=randrange(3, 10))),
                author=choice(authors),
            )
            post.pub_date = fake.date_time(timezone.utc)
            post.save()
            created_posts += 1
        except IntegrityError:
            print("Repeated posts data")
