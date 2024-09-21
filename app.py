from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from data import (get_products, get__one__products, put_feedback, get_feedback, register_user, get_users,
                  get_users_by_email, get_users_by_id, add_product, get_max_id_products, delete_product)
import random
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'qwecfcrdmlskhbmdfhagaslghsvdfjsgsj'


class User:
    def __init__(self, id, name, email, password, admin, rem=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
        self.rem = rem
        self.REMEMBER_COOKIE_DURATION = 60

    def remember(self):
        return self.rem == 'on'

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user = get_users_by_id(user_id)
    if user:
        return User(id=user[0], name=user[1], email=user[2], password=user[3],
                    admin=user[4] if len(user) > 4 else False)
    return None


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        rem = request.form.get('remember', 'off')
        list_users = get_users()
        user = None
        for i in list_users:
            if i[2] == email:
                user = i
                break
        if user:
            if check_password_hash(user[3], password):
                user_obj = User(id=user[0], name=user[1], email=user[2], password=user[3], admin=user[4], rem=rem)
                login_user(user_obj, remember=user_obj.remember())
                flash('Ви успішно увійшли!', 'success')
                return redirect(url_for('index'))
            else:
                return render_template('login.html', error=2)
        else:
            return render_template('login.html', error=1)
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


@app.route('/')
def index():
    products_list = get_products()
    return render_template('index.html',  products=products_list)


@app.route('/office')
@login_required
def office():
    user_info = get_users_by_id(current_user.id)
    print(user_info)
    return render_template('office.html', user=user_info)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Ви успішно вийшли з облікового запису.', 'success')
    return redirect(url_for('index'))


@app.route('/admin', methods=["GET", "POST"])
@login_required
def admin_panel():
    if current_user.admin != 1:
        return redirect(url_for('index'))
    if request.method == 'POST':
        name =  request.form['name']
        description =request.form['description']
        img = request.form['img']
        price = int(request.form['price'])
        number = int(request.form['number'])
        add_product(name, description, img, price, number)
    return render_template('admin.html')


@app.route('/admin/add_product', methods=["GET", "POST"])
@login_required
def add_product_route():
    if current_user.admin != 1:
        return redirect(url_for('index'))
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        img = request.form['img']
        price = int(request.form['price'])
        number = int(request.form['number'])
        add_product(name, description, img, price, number)
    return render_template('add_product.html')


@app.route('/admin/delete', methods=["GET", "POST"])
@login_required
def delete_product_route():
    if current_user.admin != 1:
        return redirect(url_for('index'))
    if request.method == 'POST':
        product_id = request.form['product_id']
        delete_product(int(product_id))

    return render_template('delete_product.html')


@app.route('/buy_product/<int:id>/', methods=["GET", "POST"])
def buy_product(id):
    max_id = get_max_id_products()
    products_list = get_products()

    if id <= max_id and id > 0:
        product = get__one__products(id)
        product_ids = [product[0] for product in products_list]
        if not product:
            return "Product not found", 404


        product_random = None
        while not product_random or product_random[0] == product[0]:
            product_random = get__one__products(random.choice(product_ids))


        feedback_list = get_feedback()
        if request.method == 'POST':
            name = request.form['name']
            feedback = request.form['feedback']
            put_feedback(name, feedback, id)
            return redirect(url_for('buy_product', id=id))

        return render_template('buy_product.html',
                               product=product,
                               product_random=product_random,
                               feedback_list=feedback_list,
                               id=id)
    else:
        return "Product not found", 404


if __name__ == "__main__":
    app.run(debug=True)