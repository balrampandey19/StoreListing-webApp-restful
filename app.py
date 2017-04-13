from flask import Flask, jsonify, request, render_template

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
@app.route("/")
def home():
    return render_template('index.html')



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
    request_data = request.get_json()
    for store in stores:
        if(store['name'] == name)
        store_item={
        'name':request_data['name'],
        'price':request_data['price']
        }
        store['items'].append(store_item)
        return jsonify(store_item)
    return jsonify({'message':'Store not found'})


@app.route("/store<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if(store['name'] == name)
        return jsonify(store['items'])
    return jsonify({'message':'Store not found'})


app.run(port=5000)
