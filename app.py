from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello world"

#POST /store data:{name:}

@app.route("/store",method=['POST'])
def create_store:
    pass

@app.route("/store<string:name>")
def get_store(name):
    pass
app.run(port=5000)
