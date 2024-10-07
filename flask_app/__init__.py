from flask import Flask , render_template , request , flash , redirect
from flask_mail import Mail , Message
app = Flask(__name__)
mail=Mail(app)
app.secret_key = "hpx"


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'Nassymhopex3@gmail.com'
app.config['MAIL_PASSWORD'] = 'pdcr jozd uglo zelu'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'Nassymhopex3@gmail.com'  
mail = Mail(app)




@app.route('/')
def home():
    return render_template('home.html')


@app.route('/send', methods=['POST'])
def send_order():
    # Fetch form data
    code = request.form.get('code')
    email = request.form.get('email')

    if not code or not email:
        flash("All fields are required!", "error")
        return redirect('/orders/{{ order.id }}')  

    # Create a message
    msg = Message('GiftCard Order Received', recipients=[email])
    msg.body = f"""
    Dear Customer,

    Thank you for your order. Here are your order details:
    GiftCard Code: {code}
    Email: {email}

    We will process your order shortly.

    Best regards,
    GiftCard Shop
    """
    
    # Send the email
    try:
        mail.send(msg)
        flash("Email sent successfully!", "success")
    except Exception as e:
        flash(f"Failed to send email. Error: {str(e)}", "error")

    return redirect('/orders')  


    

DB = "group_schema"