# Dummy CSV Generator

Dummy CSV Generator is a service for generating CSV files with fake(dummy) data.
[The project](https://dummy-csv-generator.herokuapp.com/) demo is deployed on Heroku.

## Getting started

1. Clone the project, create a virtual environment, and activate it.

```bash
git clone git@github.com:damhuman/dummyCSVGenerator.git
cd dummyCSVGenerator

python3 -m venv env
source env/bin/activate
```
2. Install dependencies from the requirements file
```bash
pip install -r requirements.txt
```

3. Set environmental variables in the virtualenv. You may use Heroku to set up Redis and Postgres, but you can run them locally instead.
```bash
export DATABASE_URL="postgres://..."
export REDIS_URL="redis://..."
export SECRET_KEY="SECRET KEY HERE"
```

Also, you can change DATABASES parameter in the settings.py file in case if you want to configure the database connection directly.
```bash
DATABASES = {
'default':{
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'django_db',
    'USER' : 'user_name',
    'PASSWORD' : 'password',
    'HOST' : '127.0.0.1',
    'PORT' : '5432',
}
```
4. You can use Amazon S3 bucket to store all generated CSV files. To do this create an S3 bucket and add needed parameters to the virtualenv. Set USE_S3="FALSE" if you want to store files locally in media directory
 ```bash
export USE_S3="TRUE"
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_STORAGE_BUCKET_NAME="..."
```
or
 ```bash
export USE_S3="FALSE"
```

## Running the project

```bash
python3 manage.py runserver
celery -A generator worker -l info
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
