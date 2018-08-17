from flask import Flask, jsonify,request,abort, Response, json

# local import
from instance.config import app_config



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
#GET ALL QUESTIONS


    qtns = [
        {
            'id': 101,
            'txt': 'what is Andela',
            'Poster': 'mozzy'
        },
        {
            'id': 201,
            'txt': 'what is a boot camp',
            'Poster': 'Arnold'
        }
    ]

    @app.route('/questions', methods=['GET'])
    def get_all_qtns():
        return jsonify({'qtns': qtns})



    return app