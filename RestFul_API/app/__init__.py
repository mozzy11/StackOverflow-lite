from flask import Flask, jsonify,request,abort, Response, json

# local import
from instance.config import app_config




def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

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

    # POST A QUESTION

    @app.route('/api/v1/questions', methods=['POST'])
    def add_qtn():

        request_qtn = request.json
        if (valid_qtn(request_qtn)):
            qtn = {
                'id': request_qtn['id'],
                'txt': request_qtn['txt'],
                'Poster': request_qtn['Poster']
            }
            qtns.append(qtn)
            response = Response("", 201, mimetype="application/json")
            response.headers['Location'] = "books/" + str(request_qtn['id'])
            print(qtns)
            return jsonify(qtn)
            # return response
        else:
            bad_object = {
                "error": "Invalid Qtn",
                "help_string":
                    "Request format should be {'id': 1,'txt': 'Where is Andela','Poster': 'Seruwu' }"

            }
            response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
            return response

    def valid_qtn(qtnObj):
        if "id" in qtnObj and "txt" in qtnObj and "Poster" in qtnObj:
            return True
        else:
            return False

    return app