from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask import app



app = Flask(__name__)

app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'dhanushrasu07@gmail.com'
app.config['MAIL_PASSWORD'] = 'gfjiklmonztiezwv'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


mail = Mail(app)


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
    


  
        msg = Message(subject='Contact Form Submission',
                      sender='dhanushrasu07@gmail.com',
                      recipients=['dhanushproject25@gmail.com'])
        msg.body = "Name: {name}\nEmail: {email}\nMessage: {message}"

    
        try:
            mail.send(msg)
            return render_template('thank.html', name=name, email=email, message=message)
        except Exception as e:
            return f"An error occurred: {str(e)}"
      
    return render_template("thank.html")

if __name__ == '__main__':
    app.run(debug=False)
