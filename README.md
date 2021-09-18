# Django Boilerplate

Custom Flow Stack template to quickly scaffold small and large scale Django projects

### Set up a Python 3.x virtual environment

```
python3 -m venv venv
source venv/bin/activate
```
Or otherwise, you can set up a virtual environment from your IDE.

### Install development requirements

```
pip install -r requirements/development.txt
```

### Set up pre-commit hook

```
pre-commit install
```

### Run migrations

```
python manage.py migrate
```

### Run the development server

```
python manage.py runserver
celery -A config worker -l INFO
```
