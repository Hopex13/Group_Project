from flask_app import app
from flask import Flask , render_template , redirect , request , session, flash
from flask_app.models.order_model import Order
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)





#================== Display Route =======================
@app.route('/register')
def log_reg():
    return render_template('dashboard.html')


#================= Action Routes ==================
@app.route('/create/user', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/register')

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    user = User.create_user(data)
    session['user_id'] = user

    return render_template('dashboard1.html')

#================= Action Routes ==================
@app.route('/login', methods=['POST'])
def login():
    user_in_db = User.get_by_email(request.form)
    if not user_in_db:
        flash("Invalid email address or password!!!", "login")
        return redirect('/login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Incorrect password!!!", "login")
        return redirect('/login')
    session['user_id'] = user_in_db.id
    return redirect('/orders')


#================== Display Route =======================
@app.route('/orders')
def dashboard():
    if 'user_id' not in session:
        return redirect('/register')
    user = User.get_by_id({'id': session['user_id']})
    all_orders = Order.get_all_orders()
    
    return render_template("index.html", user=user ,all_orders=all_orders)


#================= Action Routes ==================
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/register')


@app.route('/history')
def history():
    return render_template("history.html")


@app.route('/login')
def already():
    return render_template('dashboard1.html')

