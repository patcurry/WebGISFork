#!/bin/bash
python3 -m venv ENV
source ENV/bin/activate

# set secret environmental variables
export SECRET_KEY=`jq '.SECRET_KEY' dev-secrets.json`
export CRYPTO_KEY=`jq '.CRYPTO_KEY' dev-secrets.json`

export EMAIL_HOST=`jq '.EMAIL_HOST' other-secrets.json`
export EMAIL_PORT=`jq '.EMAIL_PORT' other-secrets.json`
export EMAIL_HOST_USER=`jq '.EMAIL_HOST_USER' other-secrets.json`
export EMAIL_HOST_PASSWORD=`jq '.EMAIL_HOST_PASSWORD' other-secrets.json`

pip install --upgrade pip
pip install -r requirements.txt

#python manage.py makemigrations
python manage.py migrate
#python manage.py test --settings=main.settings.dev
python manage.py runserver --settings=main.settings.dev
