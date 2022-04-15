from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://minji:0819@cluster0.vdsdj.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_list = list(db.buckets.find({}, {'_id': False}))
    count = len(bucket_list) + 1
    bucket_receive = request.form['bucket_give']
    doc = {
        'num': count,
        'bucket': bucket_receive,
        'done': 0
    }
    db.buckets.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.buckets.update_one({'num': int(num_receive)}, {'$set':{'done':1}}) //숫자로 바꾸기
    print(num_receive)
    return jsonify({'msg': 'bucket 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.buckets.find({}, {'_id': False}))
    return jsonify({'buckets': bucket_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)