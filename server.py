from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

@app.route('/create/')
def create():
    return 'create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'read ' + id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)