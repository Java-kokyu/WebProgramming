from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://minji:0819@Cluster0.vdsdj.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    print(name_receive, comment_receive)

    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }

    db.comments.insert_one(doc)
    return jsonify({'msg':'응원 댓글 남기기 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    all_comments = list(db.comments.find({}, {'_id': False}))
    return jsonify({'comments': all_comments});

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)