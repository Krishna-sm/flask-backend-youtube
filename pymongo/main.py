from flask import Flask,render_template,request,redirect,url_for
from flask_pymongo import PyMongo
from bson import  ObjectId
app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://127.0.0.1:27017/flask_tut"

mongodb = PyMongo(app).db

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/todo",methods=['POST'])
def add_todo():
    item = {
        "title":request.form['title'],
        "description":request.form['description'],
        "isComplete":False
    }
    mongodb.todos.insert_one(item)
    return redirect(url_for('hello'))


@app.route("/todos",methods=['GET'])
def getAll():
    array=[]
    data = mongodb.todos.find({})
    for todo in data:
        item ={
            "id":str(todo['_id']),
            "title":todo['title'],
            "description":todo['description'],
            "isComplete":todo['isComplete'],
        }
        array.append(item)
    print(array)
    # return redirect(url_for('hello'))
    return render_template('todos.html',data=array)
    # return 'hi'


@app.route("/todo/update/<string:id>")
def update_doc(id):
    todo_id = ObjectId(id)
    db =mongodb.todos.find_one_and_update({"_id":todo_id},{"$set":{"isComplete":True}})
    print(db)
    return redirect(url_for('getAll'))


@app.route("/todo/delete/<string:id>")
def delete_doc(id):
    todo_id = ObjectId(id)
    mongodb.todos.find_one_and_delete({"_id":todo_id})
    return redirect(url_for('getAll'))


if __name__ == '__main__':
    app.run(debug=True,port=3000)