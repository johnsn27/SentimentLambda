from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
 return '<h1>Hello World</h1>'

# We only need this for local development.
if __name__ == '__main__':
 app.run()