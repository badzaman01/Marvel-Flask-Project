from flask import Blueprint, render_template

"""
some arg are specified when creating the
Blueprint objects, like site. The first 
argument site is the blueprint name. Second
arg __name__ is the blueprint's import name,
which is used to locate the Blueprint's resources

"""

site = Blueprint('site', __name__, template_folder = 'site_templates')

#routing mechanism
@site.route('/') #anything under site should be returned under '/'
def home():
    return render_template('index.html')
    #render template looking for index template

@site.route('/profile')
def profile():
    return render_template('profile.html')