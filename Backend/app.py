from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

#Database connection
client = MongoClient(host='card_mongodb',port=27017)
db = client.cards
cards = db.cards

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.errorhandler(Exception)
def server_error(err):
    #we can implement logger here to save error message
    return "Error occured! ", 500

#API routes
@app.route('/')
def index():
    return "Welcome user! Use the web app to use the app"

#Get all the cards
@app.route('/cards', methods=['GET'])
def getScore():
    cards = db.cards.find()
    return dumps({
        'status': 'success',
        'cards': cards
    })

#Update the score of the given card by its card id
@app.route('/score/<card_id>', methods=['PUT'])
def update_score_byId(card_id):
    if request.method == 'PUT':
        post_data = request.get_json() 
        result = db.cards.update_one({'card_id': card_id}, {"$set": {'score': post_data.get('score')}})
        response_object = {'status': 'success'}
        response_object['res'] = result.raw_result
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)
