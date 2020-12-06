# Footprint API

## Installing requirements and creating the virtual environment

Run the command

```bash
source install.sh
```

## Database Setup

In the same directory as the manager.py file, run the command

```bash
$ $ sudo docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=admin -e POSTGRES_DBNAME=footprintDB -p 5432:5432 kartoza/postgis:9.6-2.4
```

Note: You need to have Docker installed on your system.
In the same directory as the manager.py file, run the commands:

To populate the database with our tables,

```bash
$ python manage.py makemigrations
```

```bash
$ python manage.py migrate
```

Finally, run the server

```bash
$ python manage.py runserver
```
