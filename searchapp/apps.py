from django.apps import AppConfig


class SearchappConfig(AppConfig):
    name = 'searchapp'

    # def ready(self):
    #     from . import job
    #     job.start()