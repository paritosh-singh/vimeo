from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from vimeo_assignment.utils import get_vimeo_users
from datetime import datetime


class Command(BaseCommand):
    help = 'Fetch Vimeo users and updates the database'

    def handle(self, *args, **options):
        start_time = datetime.now()
        self.stdout.write('\n\nUpdating database with new %s vimeo users : \n\n'%settings.USERS_LIMIT)
        try: get_vimeo_users()
        except Exception as e:
            raise CommandError('Error updating database : %s' % e)
        self.stdout.write('Successfully updated database with %s vimeo users \n\n'%settings.USERS_LIMIT)
        end_time = datetime.now()
        delta_time = end_time - start_time
        self.stdout.write('Time taken for updating db %s \n\n'%delta_time)