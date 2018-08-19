from flask import Flask, jsonify,request,abort, Response, json

# local import
from instance.config import app_config



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
#GET A QUESTIONS


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

    @app.route('/api/v1/questions/<int:questionId>', methods=['GET'])
    def get_qtn(questionId):
        qtn = {}
        for item in qtns:
            if item['id'] == questionId:
                qtn = {
                    'id': questionId,
                    'txt': item['txt'],
                    'Poster': item['Poster']
                }
        return jsonify(qtn)

    return app