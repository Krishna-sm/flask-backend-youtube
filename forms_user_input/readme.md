![Alt text](https://i.postimg.cc/xqr8Nmtn/flask.png)

# Forms and User Input in flask

- in flask form data access my `request` method which is inbuild in flask.

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>form</title>
</head>
<body>
            <form action="{{url_for('register')}}" method="post">
                <input type="text" name="name" placeholder="Enter Name" required     ><br>
                <input type="text" name="email" placeholder="Enter Email" required   ><br>
                <input type="checkbox" name="hobbies"  required value="foodies"  >food<br>
                <input type="radio" name="gender" value="male"  required   >
                <input type="radio" name="gender" value="femaile"  required   ><br>
                <button>submit</button>
            </form>
</body>
</html>

```

```python

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/register",methods=['POST'])
def register():
    if request.method =='POST':
        print(request.form);
        return 'thanku for contacting'
    else:
        return "no route found"



if __name__ == '__main__':
    app.run(debug=True)

```

# iterate items in frontend

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>form</title>
</head>
<body>
            <form action="{{url_for('register')}}" method="post">
                <input type="text" name="name" placeholder="Enter Name" required     ><br>
                <input type="text" name="email" placeholder="Enter Email" required   ><br>
                <input type="checkbox" name="hobbies"  required value="foodies"  >food<br>
                <input type="radio" name="gender" value="male"  required   >
                <input type="radio" name="gender" value="femaile"  required   ><br>
                <button>submit</button>
            </form>

            {% if data %}
            {% for key, value in data.items() %}  
            <tr>  
               <th> {{ key }} </th>  
               <td> {{ value }} </td>  
            </tr>  
         {% endfor %}  
            {% endif %}

</body>
</html>

```

```python

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/register",methods=['POST'])
def register():
    if request.method =='POST':
        print(request.form);
        return render_template('index.html',data=request.form)

    else:
        return "no route found"



if __name__ == '__main__':
    app.run(debug=True)

```

# abort()

- it is used to send status code 

```python


@app.route("/register",methods=['POST'])
def register():
    if request.method =='POST':
        print(request.form);
        return render_template('index.html',data=request.form)

    else:
        abort(401)



```



## Redirect and url_for methods

```python

@app.route("/login")
def login():
    return redirect(url_for('hello'))

```

# create simple api rest point

```python

@app.route("/api")
def api():
    return request.json

```