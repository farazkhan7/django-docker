# Structure of env files for development and production
## For Development
### create a file name .env.dev
```shell 
DEBUG=1
SECRET_KEY=<-!g..YOUR SECRET KEY..>
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_dev
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
#### Note: Add any other django related environment variables for development in the above file


## For Production
### create a file name .env.prod
```shell 
DEBUG=0
SECRET_KEY=<-!g..YOUR SECRET KEY..>
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_prod
SQL_USER=<POSTGRES USERNAME>
SQL_PASSWORD=<POSTGRES USER PASSWORD>
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
#### Note: Add any other django related environment variables for production in the above file

### create another file .env.prod.db
```shell
POSTGRES_USER=<POSTGRES USERNAME>
POSTGRES_PASSWORD=<POSTGRES USER PASSWORD>
POSTGRES_DB=hello_django_prod
```