# Auctionet - The Auctions Stream
School project by Jacopo Sartini and and Federico Cardano, Auctionet is a Real time auctions platform with Django ASGI.

## Install requirements:
```
pip install -r requirements.txt
```
## To database migration and superuser creation use the command:
```
  python3 manage.py migrate && python3 manage.py createsuperuser
```
## Run:
You need to have a redis server on 127.0.0.1:6379
```
  redis-server
```
So now you can start the Django server!
```
  python manage.py runserver
```
## In case of bugs please contact me.
