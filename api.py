from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return "<h1>Hello, World!</h1>"

# api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True) 
