
from flask import Blueprint, current_app

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():

    place = current_app.config['PLACE']
    return f"key: <i>{place}</i>"


