
from flask import Flask

# FOR relative link use dot
from .site.routes import site
from .api.routes import api

def dic_list(dic):
    keys = list(dic.keys())
    keys.sort(key=str.lower)
    for key in keys:
        print(key, '-', dic[key])

def create_app():
    app = Flask(__name__)
    #app = Flask(__name__, instance_relative_config=True)

    # hard code for now
    app.config.from_object('config.ConfigDev')

    app.register_blueprint(site)
    app.register_blueprint(api)

    dic_list(app.config)

    return app



