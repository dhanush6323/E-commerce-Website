from flask import Flask, render_template, request, redirect, url_for  
from flask_mail import Mail, Message

app = Flask(__name__)


users = {
    "dhanush": "dhanush123",
    "maruthu": "maruthu123",
    "santhosh": "santhosh123"
}


logged_in = None

@app.route('/')
def home():
  
    if logged_in:
        return render_template('base.html')
    else:
        
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
      
            logged_in = username
            return redirect(url_for('home'))
        else:
            return "Invalid username or password. Please try again."

    return render_template('login.html')

@app.route('/logout')
def logout():
    global logged_in
    logged_in = None
    return redirect(url_for('home'))


@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/home')
def basepage():
    return render_template('base.html')

@app.route('/category')
def categorypage():
    return render_template('category.html')

@app.route('/about_us')
def aboutuspage():
    return render_template('about_us.html')

@app.route('/contact_us')
def contactuspage():
    return render_template('contact_us.html')

@app.route('/cart')
def cartpage():
    return render_template('cart.html')

@app.route('/checkout')
def checkoutpage():
    return render_template('checkout.html')

@app.route('/order_confirmation')
def orderpage():
    return render_template('order_confirmation.html')

@app.route('/product_view')
def productviewpage():
    return render_template('product_view.html')

@app.route('/search')
def searchpage():
    return render_template('search.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank.html')

@app.route('/products')
def product_you():
    return render_template('products.html')


@app.route('/contact')
def contact_us():
    return render_template('contact_us.html')


@app.route('/contact', methods=['POST'])
def handle_contact_form():
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        return render_template('thank.html', name=name, email=email,message=message)



@app.route('/products')
def productspage():
   
    products = {
        1: {'name': 'Product 1', 'price': 100},
        2: {'name': 'Product 2', 'price': 200},
     
    }
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)