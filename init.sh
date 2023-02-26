#! /bin/sh
# User credentials
user=teacher
email=teacher@example.com
password=teacher

file=db/db.sqlite3
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$user', '$email', '$password')" | python3 manage.py shell
python3 manage.py migrate