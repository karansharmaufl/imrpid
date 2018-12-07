from flask import Flask

app = Flask(__name__)


# The route() decorator to binds a function to a URL.
@app.route("/")
def hello():
    return "WELCOME TO IMRPID"

# The route() decorator to binds a function to a URL.
@app.route("/register")
def register():
    return "IMPLEMENT REGISTER API"


# The route() decorator to binds a function to a URL.
@app.route("/login")
def login():
    return "IMPLEMENT LOGIN API"

# The route() decorator to binds a function to a URL.
@app.route("/upload")
def upload():
    return "IMPLEMENT UPLOAD API"


# The route() decorator to binds a function to a URL.
@app.route("/alluploads")
def alluploads():
    return "IMPLEMENT ALLUPLOADS API"



if __name__ == '__main__':
    app.run(debug = True)
