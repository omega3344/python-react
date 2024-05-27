from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, MongoClient
from flask_cors import CORS, cross_origin
from bson import ObjectId

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MONGO_DBNAME'] = 'guimadiesel'
#app.config['MONGO_URI']= 'mongodb://localhost/guimadiesel'
app.config['MONGO_URI']= 'mongodb+srv://omega3344:KKK691dd@cluster0.gmd3vkc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

cors = CORS(app, resources={r"/users/*": {"origins": "*"}})

try:
    mongo = MongoClient(app)
    #mongo = PyMongo(app)
    db = mongo.db.users
    print("MongoDB connection established successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")


@app.route('/users', methods=['POST'])
def createUser():
    id = db.insert_one({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    })   
    #return{}
    return jsonify(str(id.inserted_id))

@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in db.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'email': doc['email'],
            'password': doc['password']
        })
    return jsonify(users)

@app.route('/users/<id>', methods=['GET'])
def getUser(id):
    user = db.find_one({'_id': ObjectId(id)})
    return jsonify({
        '_id': str(ObjectId(user['_id'])),
        'name': user['name'],
        'email': user['email'],
        'password': user['password']
    })

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'User deleted'})

@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    db.update_one({'_id': ObjectId(id)}, {'$set': {
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
        }})
    return jsonify({'msg': 'User updated'})

if __name__ == "__main__":
    app.run(debug=True)
