from django.core.management.base import BaseCommand

from util import fixtures


class Command(BaseCommand):
    help = 'Populate database with fake data (fixtures).'

    def add_arguments(self, parser):
        parser.add_argument('authors', type=int)
        parser.add_argument('posts', type=int)

    def handle(self, **options):
        self.stdout.write('Blog Fixtures')
        fixtures.generate(
            total_authors=options['authors'],
            total_posts=options['posts']
        )
