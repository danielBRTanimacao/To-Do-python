import os
import sys
# from random import randint # OTIONAL
from pathlib import Path
# from random import choice # OPTIONAL

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 20 # Change here to the number of objects you want

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings' # change core to you BASE DIR NAME
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker 
    # Faker is a Python package that generates fake data for you
    # https://pypi.org/project/Faker/

    from ToDoApp.models import Task # import your model to add objtects

    Task.objects.all().delete() # delete all objects OPTIONAL

    fake = faker.Faker('pt_BR') # change language

    # STATUS_CHOICE = []
    # If your database requires making choices add the list here OPTIONAL

    django_objects = []

    for indc in range(NUMBER_OF_OBJECTS):
        fake_indc = fake.profile() # creating client

        # create and add all indc objects here
        exemple = fake_indc['name']

        # add incice to your object
        django_objects.append(
            Task(
               title = exemple 
            )
        )

    if len(django_objects) > 0:
        Task.objects.bulk_create(django_objects)