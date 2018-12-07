from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "WELCOME TO IMRPID"


if __name__ == '__main__':
    app.run(debug = True)
