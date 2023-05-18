#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


#TODO: Решить баг с неотображаемой картинкой на всех страницах с Parallax - готово, но с багами
#TODO: Добавить регистрацию, вход и выход с аккаунта
#TODO: Добавить модельки и объекты для Servise, Products, Testimonials, Pricing, Work
#TODO: Переделать Send us a message в комментарии и сделать это работоспособным
