from flask import Flask

app = Flask(__name__)

@app.route('/')
def initialisation():
    return {'sample':'Flask Project for test'}

if __name__ == '__main__':
    app.run(debug=True)  