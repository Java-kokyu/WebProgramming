from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://minji:0819@Cluster0.vdsdj.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta



@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']

    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }
    print(doc)
    db.mars.insert_one(doc)

    return jsonify({'msg': '주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    all_orders = list(db.mars.find({}, {'_id': False}))
    print(all_orders)
    return jsonify({'orders': all_orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)