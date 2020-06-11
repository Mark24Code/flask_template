from flask import render_template
from . import welcome

@welcome.route('/', methods=['GET', 'POST'])
def index():
    return render_template('welcome.html')