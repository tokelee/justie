from flask import Blueprint, render_template, url_for, redirect

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html', title='Justie Confectionery')

@views.route('/our-services')
def our_services():
    return render_template('our-services.html', title='Justie Confectionery - Our services')