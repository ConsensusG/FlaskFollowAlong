from flask import Blueprint, render_template

# Blueprint is a class provided by Flask that allows you to organize your application into reusable components. It helps create modular and scalable applications by grouping related routes, templates, and static files together.
# render_template is a function provided by Flask that is used to render HTML templates. It takes the name of the template file as an argument and returns the rendered HTML content.

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')