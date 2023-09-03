
from flask import Blueprint, current_app

site = Blueprint('site', __name__)

@site.route('/')
def index():

    color = current_app.config['COLOR']
    return f"<b>Site</b> {color}"


