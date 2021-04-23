from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'API'

    def ready(self):
        import API.signals


# class BaseConfig(AppConfig):
#     name = 'base'
#
#     def ready(self):
#         import base.signals

