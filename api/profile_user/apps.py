from django.apps import AppConfig


class ProfileUserConfig(AppConfig):
    name = 'profile_user'
    # под этим именем приложение будет видно в админке.
    verbose_name = 'Профайл пользователя'
