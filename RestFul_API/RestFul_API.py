from flask import Flask, jsonify,request,abort

app = Flask(__name__)

qtns=[
 {
 'id': 101,
 'txt':'what is Andela',
 'Poster':'mozzy'
 },
 {
 'id': 201,
 'txt':'what is a boot camp',
 'Poster':'Arnold'
 }
 ]
# GET a Question
@app.route('/questions/<int:questionId>' ,methods=['GET'])
def get_qtn(questionId):
    qtn = {}
    for item in qtns:
        if item['id'] == questionId:
            qtn = {
                'id'  : questionId,
                'txt': item['txt'],
                'Poster': item['Poster']
             }
    return jsonify(qtn)


app.run()