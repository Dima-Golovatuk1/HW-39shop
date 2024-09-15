from flask import Flask, render_template
from data import products, products_list
import data
import random

app = Flask(__name__)
# print(products_list)

@app.route('/')
def index():
    return render_template('index.html',  products=products)


@app.route('/buy_product/<int:id>/')
def tours(id):
    if id in products:
        num = random.randrange(1, len(products))
        return render_template('buy_product.html',
                                products = data.products[id],
                                id = id,
                                number = products[id]['number'],
                                name=products[id]['name'],
                                description=products[id]['description'], 
                                price=products[id]['price'], 
                                img=products[id]['img'], 
                                random_product=products.get(num),
                                num=num)
    else:
        return "Product not found", 404


if __name__ == "__main__":
    app.run(debug=True)