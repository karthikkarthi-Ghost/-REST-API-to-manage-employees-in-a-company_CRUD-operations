from flask import render_template, request, redirect, url_for, flash
from python.config import app, db 

@app.route('/add_customer',methods=['GET', 'POST'])
def add_customer():
    return render_template('customer.html')