# DRF Authentication

- package for authectication user with django rest framework API

### Quickstart
For installing django-drf-auth, just run this command in your shell

```
pip install django-drf-auth
```

### settings
```
INSTALLED_APPS = (
    # ...
    
    'django.contrib.sites',
    'rest_framework',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'drf_auth',
)


FRONT_URL = '' 
EMAIL_HOST_USER = '' 
EMAIL_HOST_PASSWORD = '' 
EMAIL_PORT = 587 

REST_USE_JWT = True
SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True

```
FRONT_URL -> this is your url `` https://www.example.com ``


### URLS

```
urlpatterns = [
    # ...
    path('drf_auth/', include('drf_auth.urls')),
]
```


## install celery and make celery installations 
- file : proj/proj/celery.py
```
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
```
- proj/proj/__init__.py:

```
from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)
```



#### API Endpoints: 

##### Register
Method: `POST`  
Endpoint: `/registration/`  
Payload:  
`{  
    "username": "USERNAME",  
    "password1": "PASSWORD",  
    "password2": "PASSWORD",  
    "email": "EMAIL"  
}`

##### Register Confirm Email
Method: `POST`  
Endpoint: `/account-confirm-email/<str:key>/`  
Payload:  
`{  
    "key": "KEY",
}`


##### Login
Method: `POST`  
Endpoint: `/login/`  
Payload:  
`{  
    "username": "USERNAME",  
    "password": "PASSWORD"  
}`

##### Logout
Method: `POST`  
Endpoint: `/logout/`  
Headers: `Authorization: JWT YOUR_TOKEN_HERE`  

##### Change Password
Method: `POST`  
Endpoint: `/password/change/`  
Payload:  
`{  
    "old_password": "OLD PASSWORD",  
    "new_password1": "NEW PASSWORD1",
    "new_password2": "NEW PASSWORD2"  
}`

##### Reset Password
Method: `POST`  
Endpoint: `/password/reset/`  
Payload:  
`{  
    "email": "EMAIL ADDRESS",  

}`

##### Reset Password Confirm
Method: `POST`  
Endpoint: `/password/reset/confirm/<str:uid>/<str:token>/`  
Payload:  
`{  
    "uid": "UID",  
    "token": "token",  

}`

##### Reset Password Confirm
Method: `GET`  
Endpoint: `/user/`  
Headers: `Authorization: JWT YOUR_TOKEN_HERE`  


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## PYPI

[PYPI](https://pypi.org/project/django-drf-auth/0.1/)


## License
MIT
