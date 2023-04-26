#!/bin/bash

python3 manage.py migrate
# User credentials
user=teacher
email=admin@example.com
password=12345

array_users=("analyst1" "analyst2" "response1" "response2")

file=db/db.sqlite3

echo "from django.contrib.auth.models import User; User.objects.create_superuser('$user', '$email', '$password')" | python3 manage.py shell

for usr in ${array_users[@]}; do
  echo "from django.contrib.auth.models import User; User.objects.create_user('$usr', '$email', '$password')" | python3 manage.py shell
done

python3 manage.py migrate
python3 manage.py collectstatic  --noinput --clear