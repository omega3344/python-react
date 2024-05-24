from flask import Flask
from flask_pymongo import PyMongo, MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
'''
client = MongoClient('mongodb+srv://omega3344:KKK691dd@cluster0.gmd3vkc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
try:
    client.admin.command('ping')
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
'''

app.config['MONGO_DBNAME'] = 'guimadiesel'
#app.config['MONGO_URI']= 'mongodb://127.0.0.1:27017/guimadiesel'
app.config['MONGO_URI']='mongodb+srv://omega3344:KKK691dd@cluster0.gmd3vkc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

print(f"MONGO_URI: {app.config['MONGO_URI']}")

try:
    mongo = PyMongo(app)
    db = mongo.db.users
    print("MongoDB connection established successfully.")
    print(db)
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

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
