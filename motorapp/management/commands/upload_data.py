from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
import os, sys
import json
import datetime
import numpy as np
import hashlib


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument('dir_ftm')
        parser.add_argument('dir_temp')

    def handle(self, *args, **options):
        dir_ftm = options['dir_ftm']
        dir_temp = options['dir_temp']

        dt = 0.01
        nb_header = 5
