
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Testing the command extension'

    option_list = BaseCommand.option_list + (
        make_option('--user', action='store', dest='user',
                    default=None, help='test'),
    )

    def handle(self, *args, **options):
        print "%s" % options.get('user')