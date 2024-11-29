import os
import sys
from random import randint
from pathlib import Path
from random import choice

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

    STATUS_CHOICE = ['Aguardando', 'Processando', 'Enviado', 'Entregue', 'Cancelado']
    # If your database requires making choices add the list here OPTIONAL

    django_objects = []

    for indc in range(NUMBER_OF_OBJECTS):
        client = fake.profile() # creating client

        # indices obj
        name = client['name']
        product = products[indc]
        amount = randint(0, 100)
        total_price = values_products[indc]
        status = choice(STATUS_CHOICE)

        django_objects.append(
            Order(
                client=name,
                product=product,
                amount=amount,
                total_price=total_price,
                status=status,
            )
        )

    if len(django_objects) > 0:
        Order.objects.bulk_create(django_objects)