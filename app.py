from flask import Flask, render_template
from data import get_products, get__one__products
import random

app = Flask(__name__)
# print(products_list)

@app.route('/')
def index():
    products_list = get_products()
    return render_template('index.html',  products=products_list)


@app.route('/buy_product/<int:id>/')
def tours(id):
    print(id)
    products_list = get_products()
    product = get__one__products(id-1)
    num = random.randrange(1, len(products_list))
    product_random = get__one__products(num)
    
    if id <= len(products_list) and id > 0:
        num = random.randrange(1, len(products_list))
        return render_template('buy_product.html',
                                product = product,
                                product_random = product_random)
    else:
        return "Product not found", 404


if __name__ == "__main__":
    app.run(debug=True)