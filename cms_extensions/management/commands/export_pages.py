from django.core.management.base import BaseCommand
from cms.models.pagemodel import Page
from ...utils import export_page


class Command(BaseCommand):
    def handle(self, *args, **options):
        for page in Page.objects.public():
            for language in page.get_languages():
                export_page(page, language=language)
