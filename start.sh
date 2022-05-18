export SECRET_KEY= 'secret'
export MAIL_USERNAME='maryatieno@gmail.com'
export MAIL_PASSWORD='4567'

export FLASK_APP='app:create_app("development")'
# change the command from server to run
python manage.py run


#how to run the app:
#  env FLASK_APP='app:create_app("development")' flask run
#how to initialize db:
#  env FLASK_APP='app:create_app("development")' flask db init

#how to migrate:
#  env FLASK_APP='app:create_app("development")' flask db migrate

#how to upgrade db:
#  env FLASK_APP='app:create_app("development")' flask db upgrade