from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from data import get_products, get__one__products, put_feedback, get_feedback, register_user
import random

app = Flask(__name__)
# print(products_list)

@app.route('/')
def index():
    products_list = get_products()
    return render_template('index.html',  products=products_list)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        hash = generate_password_hash(request.form['password'])
        print(name, email, hash)
        register_user(name, email, hash)
        return render_template('login.html')
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