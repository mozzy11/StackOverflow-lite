from flask import Flask, jsonify,request,abort

app = Flask(__name__)

qtns=[
 {
 'id':101,
 'txt':'what is Andela',
 'Poster':'mozzy'
 },
 {
 'id':201,
 'txt':'what is a boot camp',
 'Poster':'Arnold'
 }
 ]
@app.route('/questions' ,methods=['GET'])
def get_all_qtns():
    return jsonify({'qtns': qtns})


app.run()
