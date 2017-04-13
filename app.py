from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
{
'name':"My Wonderful name",
'items':[
{
'name':"My store item",
'price':444.32
}

]
}

]

# @app.route("/")
# def home():
#     return "Hello world"

#POST /store data:{name:}

@app.route("/store",methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
    'name':request_data['name'],
    'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route("/store<string:name>")
def get_store(name):
    for store in stores:
        if(store['name'] == name)
        return jsonify(store)
    return jsonify({'message':'Store not found'})

@app.route("/store")
def get_stores():
    return jsonify({'stores':stores})

@app.route("/store<string:name>/item",methods=['POST'])
def create_item_in_store():
    pass

@app.route("/store<string:name>/item")
def get_item_in_store(name):
    pass


app.run(port=5000)
