from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/mydb'
mongodb = PyMongo(app).db


@app.route("/api/v1/todo",methods=['GET','POST'])
def fun():
    if request.method =='POST':
        item = {}
        item['title'] = request.json['title']
        item['desc']  = request.json['desc']
        item['isComplete']  = False
        mongodb.todos.insert_one(item)
        return {"msg":"todo add successfully"}
    else:
        todos = mongodb.todos.find({})
        item =[]
        for todo in todos:
            items={
                "id":str(todo['_id']),
                "title":todo['title'],
                "desc":todo['desc'],
                "isComplete":todo['isComplete'],
            }
            item.append(items)
        return jsonify(item)



@app.route("/api/v1/todo/<string:id>",methods=['PUT','DELETE'])
def fun1(id):
    if request.method =='PUT':
        mongoid=ObjectId(id)
        mongodb.todos.find_one_and_update({"_id":mongoid},{"$set":{"isComplete":True}})
        return {"msg":"todo update successfully"}

    else:
        mongoid=ObjectId(id)
        mongodb.todos.find_one_and_delete({"_id":mongoid})
        return {"msg":"todo delete successfully"}


if __name__ == '__main__':
    app.run(debug=True)