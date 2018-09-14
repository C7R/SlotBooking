rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
sqlite3 db.sqlite3 < in.sql