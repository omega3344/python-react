from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['MONGO_URI']='mongodb://localhost/pythonractdb'
mongo = PyMongo(app)

db = mongo.db.users

@app.route('/users', methods=['POST'])
def createUser():
    return 'received'

@app.route('/users', methods=['GET'])
def getUsers():
    return 'received'

@app.route('/user/<id>', methods=['GET'])
def getUser():
    return 'received'

@app.route('/user/<id>', methods=['GET'])
def deleteUser():
    return 'received'

@app.route('/users/<id>', methods=['PUT'])
def updateUser():
    return 'received'

if __name__ == "__main__":
    app.run(debug=True)
