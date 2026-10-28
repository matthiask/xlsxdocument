SECRET_KEY = "tests"
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.auth"]
USE_TZ = True
TIME_ZONE = "Europe/Zurich"
