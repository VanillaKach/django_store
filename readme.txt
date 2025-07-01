(.venv) ubuvan@ubuvan:~/Py/django_store$ deactivate
ubuvan@ubuvan:~/Py/django_store$ rm -rf ~/Py/django_store/.venv
ubuvan@ubuvan:~/Py/django_store$ python -m venv .venv
Команда «python» не найдена. Возможно, вы имели в виду:
  команда 'python3' из deb-пакета python3
  команда 'python' из deb-пакета python-is-python3
ubuvan@ubuvan:~/Py/django_store$ python3 -m venv .venv
ubuvan@ubuvan:~/Py/django_store$ source .venv/bin/activate
(.venv) ubuvan@ubuvan:~/Py/django_store$ pip install --upgrade pip
Requirement already satisfied: pip in ./.venv/lib/python3.12/site-packages (24.0)
Collecting pip
  Using cached pip-25.1.1-py3-none-any.whl.metadata (3.6 kB)
Using cached pip-25.1.1-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-25.1.1
(.venv) ubuvan@ubuvan:~/Py/django_store$ pip install django==4.2.7 psycopg2-binary
Collecting django==4.2.7
  Using cached Django-4.2.7-py3-none-any.whl.metadata (4.1 kB)
Collecting psycopg2-binary
  Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting asgiref<4,>=3.6.0 (from django==4.2.7)
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from django==4.2.7)
  Using cached sqlparse-0.5.3-py3-none-any.whl.metadata (3.9 kB)
Using cached Django-4.2.7-py3-none-any.whl (8.0 MB)
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
Using cached sqlparse-0.5.3-py3-none-any.whl (44 kB)
Installing collected packages: sqlparse, psycopg2-binary, asgiref, django
Successfully installed asgiref-3.8.1 django-4.2.7 psycopg2-binary-2.9.10 sqlparse-0.5.3
(.venv) ubuvan@ubuvan:~/Py/django_store$ ls -la .venv/lib/python3.12/site-packages/django/db/migrations/
итого 272
drwxrwxr-x 4 ubuvan ubuvan  4096 июл  1 16:56 .
drwxrwxr-x 6 ubuvan ubuvan  4096 июл  1 16:56 ..
-rw-rw-r-- 1 ubuvan ubuvan 78977 июл  1 16:56 autodetector.py
-rw-rw-r-- 1 ubuvan ubuvan  1204 июл  1 16:56 exceptions.py
-rw-rw-r-- 1 ubuvan ubuvan 18923 июл  1 16:56 executor.py
-rw-rw-r-- 1 ubuvan ubuvan 13055 июл  1 16:56 graph.py
-rw-rw-r-- 1 ubuvan ubuvan    97 июл  1 16:56 __init__.py
-rw-rw-r-- 1 ubuvan ubuvan 16863 июл  1 16:56 loader.py
-rw-rw-r-- 1 ubuvan ubuvan  9767 июл  1 16:56 migration.py
drwxrwxr-x 3 ubuvan ubuvan  4096 июл  1 16:56 operations
-rw-rw-r-- 1 ubuvan ubuvan  3255 июл  1 16:56 optimizer.py
drwxrwxr-x 2 ubuvan ubuvan  4096 июл  1 16:56 __pycache__
-rw-rw-r-- 1 ubuvan ubuvan 13330 июл  1 16:56 questioner.py
-rw-rw-r-- 1 ubuvan ubuvan  3535 июл  1 16:56 recorder.py
-rw-rw-r-- 1 ubuvan ubuvan 13560 июл  1 16:56 serializer.py
-rw-rw-r-- 1 ubuvan ubuvan 40654 июл  1 16:56 state.py
-rw-rw-r-- 1 ubuvan ubuvan  4401 июл  1 16:56 utils.py
-rw-rw-r-- 1 ubuvan ubuvan 11458 июл  1 16:56 writer.py
(.venv) ubuvan@ubuvan:~/Py/django_store$ sudo -u postgres psql <<EOF
DROP DATABASE IF EXISTS django_store_new;
CREATE DATABASE django_store_new;
CREATE USER django_user WITH PASSWORD '8462975130';
ALTER ROLE django_user SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE django_store_new TO django_user;
\q
EOF
[sudo] пароль для ubuvan:
DROP DATABASE
CREATE DATABASE
ERROR:  role "django_user" already exists
ALTER ROLE
GRANT
(.venv) ubuvan@ubuvan:~/Py/django_store$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
(.venv) ubuvan@ubuvan:~/Py/django_store$ find . -path "*/migrations/*.pyc" -delete
(.venv) ubuvan@ubuvan:~/Py/django_store$ python manage.py makemigrations
Traceback (most recent call last):
  File "/home/ubuvan/Py/django_store/manage.py", line 18, in <module>
    main()
  File "/home/ubuvan/Py/django_store/manage.py", line 14, in main
    execute_from_command_line(sys.argv)
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 275, in fetch_command
    klass = load_command_class(app_name, subcommand)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 48, in load_command_class
    module = import_module("%s.management.commands.%s" % (app_name, name))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/commands/makemigrations.py", line 11, in <module>
    from django.db.migrations import Migration
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/db/migrations/__init__.py", line 1, in <module>
    from .migration import Migration, swappable_dependency  # NOQA
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'django.db.migrations.migration'
(.venv) ubuvan@ubuvan:~/Py/django_store$ python manage.py migrate
Traceback (most recent call last):
  File "/home/ubuvan/Py/django_store/manage.py", line 18, in <module>
    main()
  File "/home/ubuvan/Py/django_store/manage.py", line 14, in main
    execute_from_command_line(sys.argv)
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 275, in fetch_command
    klass = load_command_class(app_name, subcommand)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 48, in load_command_class
    module = import_module("%s.management.commands.%s" % (app_name, name))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/commands/migrate.py", line 9, in <module>
    from django.db.migrations.autodetector import MigrationAutodetector
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/db/migrations/__init__.py", line 1, in <module>
    from .migration import Migration, swappable_dependency  # NOQA
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'django.db.migrations.migration'
(.venv) ubuvan@ubuvan:~/Py/django_store$ python manage.py createsuperuser
Traceback (most recent call last):
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 255, in fetch_command
    app_name = commands[subcommand]
               ~~~~~~~~^^^^^^^^^^^^
KeyError: 'createsuperuser'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/ubuvan/Py/django_store/manage.py", line 18, in <module>
    main()
  File "/home/ubuvan/Py/django_store/manage.py", line 14, in main
    execute_from_command_line(sys.argv)
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 262, in fetch_command
    settings.INSTALLED_APPS
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/conf/__init__.py", line 102, in __getattr__
    self._setup(name)
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/conf/__init__.py", line 89, in _setup
    self._wrapped = Settings(settings_module)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/conf/__init__.py", line 217, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/ubuvan/Py/django_store/django_store/settings.py", line 2, in <module>
    from dotenv import load_dotenv
ModuleNotFoundError: No module named 'dotenv'
(.venv) ubuvan@ubuvan:~/Py/django_store$ python manage.py runserver
Traceback (most recent call last):
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/base.py", line 412, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/commands/runserver.py", line 74, in execute
    super().execute(*args, **options)
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/base.py", line 458, in execute
    output = self.handle(*args, **options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/commands/runserver.py", line 81, in handle
    if not settings.DEBUG and not settings.ALLOWED_HOSTS:
           ^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/conf/__init__.py", line 102, in __getattr__
    self._setup(name)
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/conf/__init__.py", line 89, in _setup
    self._wrapped = Settings(settings_module)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/conf/__init__.py", line 217, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/ubuvan/Py/django_store/django_store/settings.py", line 2, in <module>
    from dotenv import load_dotenv
ModuleNotFoundError: No module named 'dotenv'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/ubuvan/Py/django_store/manage.py", line 18, in <module>
    main()
  File "/home/ubuvan/Py/django_store/manage.py", line 14, in main
    execute_from_command_line(sys.argv)
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/core/management/base.py", line 425, in run_from_argv
    connections.close_all()
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/utils/connection.py", line 84, in close_all
    for conn in self.all(initialized_only=True):
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/utils/connection.py", line 76, in all
    return [
           ^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/utils/connection.py", line 73, in __iter__
    return iter(self.settings)
                ^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/utils/functional.py", line 57, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/utils/connection.py", line 45, in settings
    self._settings = self.configure_settings(self._settings)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/db/utils.py", line 148, in configure_settings
    databases = super().configure_settings(databases)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/utils/connection.py", line 50, in configure_settings
    settings = getattr(django_settings, self.settings_name)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/conf/__init__.py", line 102, in __getattr__
    self._setup(name)
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/conf/__init__.py", line 89, in _setup
    self._wrapped = Settings(settings_module)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuvan/Py/django_store/.venv/lib/python3.12/site-packages/django/conf/__init__.py", line 217, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/ubuvan/Py/django_store/django_store/settings.py", line 2, in <module>
    from dotenv import load_dotenv
ModuleNotFoundError: No module named 'dotenv'
(.venv) ubuvan@ubuvan:~/Py/django_store$
