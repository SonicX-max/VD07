import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'your_secret_key'  # Замените на ваш секретный ключ
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False