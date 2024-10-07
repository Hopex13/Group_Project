from flask_app import app
from flask import Flask, render_template, redirect , session, request , flash
from flask_app.models.user_model import User
from flask_app.models.order_model import Order


#==================== Display Route ==============================
@app.route('/orders/new')
def new_order():
    return render_template('order_create.html')


#==================== Actions Route ==============================

@app.route('/orders/add' , methods=['POST'])
def create_order():
    # if not Order.validate_order(request.form):
        # return redirect('/orders/new')
    order_data = {
        **request.form,
        'user_id': session['user_id']
    }
    Order.create_order(order_data)
    return redirect('/orders')


#==================== Display Route ==============================

@app.route('/orders/edit/<int:order_id>')
def edit_order(order_id):
    if 'user_id' not in session:
        return redirect('/orders')
    order = Order.get_orders_by_id({'id': order_id})
    session['order_id'] = order_id
    return render_template('edit_order.html', order=order)



#==================== Actions Route ==============================
@app.route('/orders/update/<int:order_id>', methods=['GET','POST'])
def update_order(order_id):
    if 'user_id' not in session:
        return redirect('/')
    # if not Order.validate_order(request.form):
        # return redirect(f'/order/edit/{order_id}')
    order_data = {
        **request.form,
        'id': order_id
    }
    Order.update_order(order_data)
    return redirect('/orders')


#==================== Actions Route ==============================
@app.route('/orders/delete/<int:order_id>')
def delete_order(order_id):
    Order.delete_order({'id': order_id})
    return redirect('/orders')




#==================== Actions Route ==============================

@app.route('/orders/<int:order_id>')
def show_one_order(order_id):
    if 'user_id' not in session:
        return redirect('/orders')
    order = Order.get_orders_by_id({'id': order_id})
    user = User.get_by_id({'id': session['user_id']})
    return render_template('proceed.html', order=order, user=user)


