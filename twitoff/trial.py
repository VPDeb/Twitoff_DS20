# from os import getenv
# from flask import Flask, render_template, request
# from .models import DB, User, Tweet
# from .twitter import get_user, add_or_update_user
# ​
# ​
# def create_app():
#     app = Flask(__name__)
    
#     app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# ​
#     DB.init_app(app)
# ​
#     @app.route('/')
#     def root():
#         DB.drop_all()
#         DB.create_all()
# ​
#         users = User.query.all()
#         return render_template('base.html', title='Home', users=users)
# ​
#     @app.route('/user/<username>')
#     def user(username):
        
#         return f"Hello, my name is {username}"
# ​
#     @app.route('/update')
#     def update():
#         reset()
#         insert_temp_users()
#         return render_template('base.html', title='Home',users=User.query.all())
# ​
#     @app.route('/reset')
#     def reset():
#         DB.drop_all()
#         DB.create_all()
#         return render_template('base.html', title='Home')
# ​
#     @app.route('/add', methods=['GET', 'POST'])
#     def add():
#         if request.method == 'POST':
#             get_user(request.form['text'])
#         return render_template('base.html', title='Home',users=User.query.all())
# ​
#     return app
# ​
# def insert_temp_users():
#     get_user('nasa')
#     get_user('elonmusk')