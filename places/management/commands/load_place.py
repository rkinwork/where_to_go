from django.core.management.base import BaseCommand, CommandError

from ._load_place import URLType, load_place_from_url


class Command(BaseCommand):
    help = 'Импорт одной локации в формате JSON'

    def add_arguments(self, parser):
        parser.add_argument(
            'place_json_url',
            nargs='+',
            type=URLType())

    def handle(self, *args, **options):
        for place_json_url in options['place_json_url']:
            self.stdout.write(f'loading from {place_json_url}')
            try:
                load_place_from_url(place_json_url)
            except CommandError as e:
                self.stdout.write(
                    self.style.ERROR(e)
                )
                continue
            self.stdout.write(
                self.style.SUCCESS(f'Successfully load place "{place_json_url}"')
            )
