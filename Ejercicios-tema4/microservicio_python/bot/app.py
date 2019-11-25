from flask import Flask
from flask import Response
from flask import jsonify, make_response
from playhouse.shortcuts import model_to_dict
import json
from bot.model.BaseModel import db
from bot.model.Result import Result
from bot.service.ResultService import ResultService as rService

db.init('dercn75nklk4a6', host='ec2-54-246-92-116.eu-west-1.compute.amazonaws.com', user='awolxnvarfbuje', password='50af008532aaf685ecf1e4bc9d397528354600f3de0a41554cf8291284b0eb93')
db.create_tables([Result])
app = Flask(__name__)


@app.route('/')
def recolect():
    rService.inserDataResult()
    return 'Datos recolectados'

@app.route('/insert')
def insert():
    response = rService.addResult()

    if (response == True):
        return "true"
    else:
        return "false"

@app.route('/result/<id>')
def getResult(id):

    result = rService.getResult(int(id))

    if(result is None):
        return jsonify(None)
    return jsonify(model_to_dict(result))

@app.route('/resultlocal/<local>')
def getResultBylocal(local):

    result = rService.getResultByLocal(local)

    if(result is None):
        return jsonify(None)
    return jsonify(model_to_dict(result))

@app.route('/resultvisit/<visit>')
def getResultByVisit(visit):

    result = rService.getResultByVisit(visit)

    if(result is None):
        return jsonify(None)
    return jsonify(model_to_dict(result))

@app.route('/resultall')
def getAllResult():

    result = rService.getAll()

    if(result is None):
        return jsonify(None)

    resultList= []
    for item in result:
       resultList.append(model_to_dict(item))

    print(resultList)
    return make_response(jsonify(resultList), 200)

if __name__ == '__main__':
    app.run(debug=True)