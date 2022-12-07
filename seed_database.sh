rm db.sqlite3
rm -rf ./waverapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations waverapi
python3 manage.py migrate waverapi
python3 manage.py loaddata users
python3 manage.py loaddata waver_users
python3 manage.py loaddata gear_types
python3 manage.py loaddata manufacturers
python3 manage.py loaddata specifications
python3 manage.py loaddata gear
python3 manage.py loaddata reviews
python3 manage.py loaddata posts
python3 manage.py loaddata comments
python3 manage.py loaddata gear_specs
python3 manage.py loaddata user_gear

