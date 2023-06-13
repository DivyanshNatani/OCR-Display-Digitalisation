## Django Database

This is REST Django framework used to store information in database(in our case, sqlite3, but can be extended to MySQL and other databases) as well as providing as REST APIs for inteacting with database. Django comes handy with its admin panel that allows us to see and visualise data.

## Django Installation
```
pip install django
pip install djangorestframework
```
This will install Django package on your computer, if not already installed. After this you can run following commands to run the server
```
cd .\reading_database
python manage.py runserver
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

This will print following messages and server will start on 8000 port.

To setup an admin account, follow these commands in reading_database folder

```
python manage.py createsuperuser
```
Follow on and create userID and password for admin account

After creating the account, you can access admin account on http://127.0.0.1:8000/admin

- If db.sqlite3 is currupted or you want to start with fresh database, then delete the db.sqlite3 file and type in following commands
```
python manage.py makemigrations
python manage.py migrate
```

