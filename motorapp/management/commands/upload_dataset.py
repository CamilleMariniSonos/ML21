from django.core.management.base import BaseCommand
from django.core.files import File
import hashlib
from motorapp.models import Dataset

class Command(BaseCommand):
    help = 'run: python manage upload_dataset dataset_file dataset_description'

    def add_arguments(self, parser):
        parser.add_argument('dataset_file')
        parser.add_argument('dataset_description')

    def handle(self, *args, **options):
        dataset_file = options['dataset_file']
        dataset_description = options['dataset_description']

        if not Dataset.objects.filter(description=dataset_description):
            try:
                dataset = Dataset(description=dataset_description)
                reopen = open(dataset_file, 'rb')
                #TODO: add some checks of file format and content, and modify if necessary
                django_file = File(reopen)
                dataset.raw_data.save(hashlib.sha256('raw_data_' + str(dataset.pk)). \
                                      hexdigest().encode('utf8').encode('utf-8'), \
                                      django_file, save=True)
                dataset.save()
            except:
                print 'oups, something went wrong while uploading the dataset'
        else:
            print 'oups, this dataset description already exists, change it!'
