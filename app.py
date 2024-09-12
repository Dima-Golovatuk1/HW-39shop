from flask import Flask, render_template
from data import products
import data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',  products=products)


@app.route('/buy_product/<int:id>/')
def tours(id):
    if id in products:
        return render_template('buy_product.html',
                                products = data.products[id],
                                name=products[id]['name'],
                                description=products[id]['description'], 
                                price=products[id]['price'], 
                                img=products[id]['img'])
    else:
        return "Product not found", 404


if __name__ == "__main__":
    app.run(debug=True)