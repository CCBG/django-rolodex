# django-rolodex

Small Django example project to teach and show some generic solutions to django problems. Some of the core files have been changed to make it easier to deploy the system in a production environment as described below in section **django-modifications**


## Intallation/setup

To use the django-rolodex app relies on a couple of python packages:

* django (version 1.9.13)
* django_widget_tweaks (version 1.4.1)
* django_debug_toolbar (version 1.4)

These can easily be installed using pip:
``` bash
# install the latest version:
pip install django=1.9.13
# or a specific version
pip install django=1.9.13
```

if one or both are installed in a non-routine place change your shell setting to reflect this by setting the PYTHONPATH to an appropriate value

For the production environment the path to libraries installed in unusual places can be tweaked in the wsgi.py file.

### Download/Installation of django-rolodex

Fetch the repositiory either by downloading from github and uncompress it or clone it using git

``` bash
git clone git@github.com:CCBG/django-rolodex.git
```


### initialise the databases/

The django-rolodex reliant on two databases, one for users and sessions, and the other contains the rolodex specific information. To initialise the databases:

```bash
# update the definitions of the database if any changes have been made
python manage makemigrations

# initialise the django database:
python manage migrate

# And the rolodex specific database:
python manage migrate --database=rolodex_db

```

Django knows when to use what database by use the django_example/router.py file that tells it to use the rolodex_db for anything related to the rolodex app, and for everything else use the default database.

### run the django development server
