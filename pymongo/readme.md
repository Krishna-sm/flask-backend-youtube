# Flask PyMongo


configure flask_pymongo

```python

from flask import Flask,render_template,request,jsonify,redirect,url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/mydb'
db = PyMongo(app).db

```

## insert document in mongodb

```python

def insertDocument():
    db.<collection_name>.insert_one({"name":"Krishna"})

```
# delete document in mongodb

```python
from bson import ObjectId

db.<collection_name>.find_one_and_delete({"_id":ObjectId(id)})

```

# update docuement in mongodb

```python

users = db.<collection_name>.find_one_and_update({'_id':ObjectId(id)},{"$set":{"password":""}})
print(users)

```

# get all document with flask pymongo


```python
data = []
users = db.<collection_name>.find({})

for user in users:
    item={
        "id":user['_id'],
        "name":user['name'],
        "email":user['email'],
    }
    data.append(item)
return data 


```

# get one document with flask pymongo

```python

 user_id= ObjectId(id)
    print(user_id)
    users = db.users.find_one({'_id':user_id})
    # print(users)
    users['_id']= str(users['_id'])
    return jsonify(users)
```