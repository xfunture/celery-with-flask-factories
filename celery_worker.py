# -*- encoding: utf-8 -*-
from factories.asyn import create_celery
from factories.application import create_application

celery = create_celery(create_application())
