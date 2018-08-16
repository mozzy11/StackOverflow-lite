from flask import Flask, jsonify,request,abort, Response, json

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

#POST An answer

@app.route('/questions/<int:questionId>/answers', methods=['POST'])
def add_ans(questionId):

    request_ans = request.json
    if (valid_ans(request_ans) ):
        if any(d['id'] == questionId for d in qtns):
              ans = {
             'id': request_ans['id'],
             'txt': request_ans['txt'],
             'qtnId': questionId
             }
              ansz.append(ans)
              print(ansz)
              return jsonify(ansz)
              #return response
        else :
            bad_object = {
                "error": "The Question doesnt exist",
                "help_string":
                    " Pleae Post to an existing Question id"}

            response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
            return response

    else:
        bad_object = {
            "error": "Invalid book object",
            "help_string":
                "Request format should be {'id': 1,'txt': ' Andela is good','qtnid': 101 }"

        }
        response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
        return response


def valid_ans(ansObj):
    if "id" in ansObj and "txt" in ansObj and "qtnId" in ansObj:
        return True
    else:
        return False

ansz=[
 {
 'id':1000,
 'txt':'Andela is a Training and Facilitation Center for young Programmers',
 'qtnId': 101
 }

]

app.run()