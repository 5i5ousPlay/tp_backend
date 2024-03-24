# Setup

Note: Please activate your virtual environment beforehand. 

1. `pip install -r requirements.txt`
2. Set up your `.env` file.

```
SECRET_KEY = 'secret_key'
DEBUG = True
DB_NAME = 'tp_postgres'
DB_USER = 'db_user'
DB_PASSWORD = 'db_pass'
DB_HOST = 'localhost'
DB_PORT = '5432'
``````

3. `python manage.py loaddata test_data/*`

Congratulations!

**For Back-End API Documentation please see:** https://taepare.atlassian.net/l/cp/pJvDz3cJ

**Please make sure you have a Confluence acc and are in the Tae Pare Dev Team**
