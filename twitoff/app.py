"""Main app/routing file for Twitoff"""

from os import getenv
from flask import Flask, render_template, request
from .models import DB, User
from .twitter import add_or_update_user, update_all_users
from .predict import predict_user


#creates application
def create_app():
    """Creating and configuring an instance of the Flask application"""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    @app.route('/')
    def root():

        users = User.query.all()
        return render_template('base.html', title='home', users=users)


    @app.route('/compare',methods=['POST'])
    def compare():
        user0, user1 = sorted([request.values['user1'], request.values['user2']])

        if user0 == user1:
            message = 'Can not compare users to themselves!'

        else:
            prediction = predict.user(user0, user1, request.values['tweet_text'])
            message = '{} is more likely to be said by {} than {}'.format(
                request.values['tweet_text'], user1 if prediction else user0, 
                user0 if prediction else user1
            )

    @app.route('/user', methods=['POST'])

    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name or request.values['user_name']
        try:
            if request.method == 'POST':
               add_or_update_user(name)
               message = 'User {} was successfully added!'.format(name)

            tweets = User.query.filter(User.name == name).one().tweets
        
        except Exception as e:
            message = 'Error adding {}: {}'.format(name, e)
            tweets = []
        return render_template('user.html', title='name', tweets=tweets, message=message)


    @app.route('/update')
    def update():
        reset()
        update_all_users()
        return render_template('base.html', title="home", users=User.query.all())

    @app.route('/reset')
    def reset():
        DB.drop.all()
        DB.create_all()
        return render_template('base.html', users=User.query.all(), title='All Tweets updated!')
    return app

# def insert_example_users():
#     add_or_update_user('elonmusk')
#     add_or_update_user('nasa')