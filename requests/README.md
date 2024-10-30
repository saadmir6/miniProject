# Project Title

A brief description of your project goes here.

## Requirements

Make sure you have Python installed on your machine. You can then install Django and other necessary packages using pip.

```bash
pip install django
pip install django-widget-tweaks


python manage.py startapp requests

python manage.py makemigrations
python manage.py migrate

python manage.py runserver


```
Create users in shell using 

```bash
python manage.py shell

# from django.contrib.auth.models import User

# User.objects.create_user(username='CSO', password='CSO123')
# User.objects.create_user(username='SCSO', password='SCSO123')
# User.objects.create_user(username='finance', password='finance123')
# User.objects.create_user(username='administration', password='admin123')
# User.objects.create_user(username='service_manager', password='service123')
# User.objects.create_user(username='subteams', password='subteams123')
# User.objects.create_user(username='production_manager', password='prod123')
# User.objects.create_user(username='hr_manager', password='hr123')

```