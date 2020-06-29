from config import Config
from flask import Flask
from flask_pymongo import PyMongo


config = Config()
app = Flask(__name__)
app.config['MONGO_URI'] = config.config['MONGO']['URI'][1:-1]
mongo = PyMongo(app)

@app.route('/')
def hello():
  return {'status': '200'}

if __name__ == '__main__':
  app.run(debug=True)
