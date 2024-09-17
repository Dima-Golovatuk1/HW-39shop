from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from data import (get_products, get__one__products, put_feedback, get_feedback, register_user, get_users,
                  get_users_by_email)
from user_login import UserLogin
import random

app = Flask(__name__)
app.secret_key = 'sdsgagsagsduipvnols'


login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromdb(user_id)



@app.route('/')
def index():
    products_list = get_products()
    return render_template('index.html',  products=products_list)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = get_users_by_email(request.form['email'])
        if user and check_password_hash(user[3], request.form['password']):


    return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        hash = generate_password_hash(request.form['password'])
        user_list = get_users()
        password = request.form['password']
        confirm_password = request.form['password2']
        if password == confirm_password:
            for i in user_list:
                if email != i[2]:
                    print(name, email, hash)
                    register_user(name, email, hash)
                    return render_template('login.html')
                else: return render_template('register.html', error='Вибачте але такий емеїл вже існує,')
        else: return render_template('register.html', error='Ви вказали не вірний пароль')
    return render_template('register.html')


@app.route('/buy_product/<int:id>/', methods=["GET", "POST"])
def buy_product(id):
    products_list = get_products()
    if id <= len(products_list) and id > 0:
        product = get__one__products(id - 1)
        num = random.randrange(1, len(products_list))
        product_random = get__one__products(num)
        feedback_list = get_feedback()
        
        if request.method == 'POST':
            name = request.form['name']
            feedback = request.form['feedback']
            put_feedback(name, feedback, id)
            return redirect(url_for('buy_product', id=id))
        
        return render_template('buy_product.html',
                                product=product,
                                product_random=product_random,
                                feedback_list=feedback_list)
    else:
        return "Product not found", 404


if __name__ == "__main__":
    app.run(debug=True)