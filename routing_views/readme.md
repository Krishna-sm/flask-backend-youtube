![Alt text](https://i.postimg.cc/xqr8Nmtn/flask.png)

# Routing and Views

- In the Flask Routing is Inbuilt , we can easily create route with methods like get post etc.
- in the flask views responsiblity is to conditionaly rendered data as route demand


1. Create a Simple Route To Print Radhey Radhey

```py
        
        from flask import Flask

        app = Flask(__name__)
        @app.route("/")
        def helloWorld():
            return "Radhey Radhey" 
        app.run(debug=True)


```


- if we need to render a .html file in the templates folder , we need a method called `render_template` to render a file

2. Create a Simple Route To render a template called   `index.html`

```py
        
        from flask import Flask,render_template

        app = Flask(__name__)
        @app.route("/")
        def helloWorld():
            return render_template('index.html') 
        app.run(debug=True)


```

`template/index.html`

```html
       
       <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello Radha</h1>
</body>
</html>
        


```

- passsing a dynamic data to frontend to server so we pass like that

3. Passing name 

```py
        
        from flask import Flask,render_template

        app = Flask(__name__)
        @app.route("/")
        def helloWorld():
            return render_template('index.html',name="Krishna") 
        app.run(debug=True)


```

```html

    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello {{name}}</h1>
</body>
</html>
```


# ***Dynamic Routing***
It is the process of getting dynamic data(variable names) in the URL and then using it

syntax:

`<converter:variable_name>`


without convertor
```python

@app.route("/user/<id>")
def helloKrishna1(id):
    print(id)
    return render_template('users.html')


```

- passing a id variable as a params type int

```python

@app.route("/user/<int:id>")
def helloKrishna1(id):
    print(id)
    return render_template('users.html')


```


- passing a name variable as a params type string

```python

@app.route("/user/<string:name>")
def helloKrishna1(name):
    print(name)
    return render_template('users.html')


```




- passing a marks variable as a params type float

```python

@app.route("/user/<float:marks>")
def helloKrishna1(marks):
    print(marks)
    return render_template('users.html')


```



- passing a path variable as a params type path



```python

@app.route("/user/<path:path>")
def helloKrishna1(path):
    print(path)
    return render_template('users.html')


```


- passing multiple variables as a params 

example:


```python

@app.route("/user/<int:id>/<string:name>")
def helloKrishna1(id,name):
    print(id)
    print(name)
    return render_template('users.html')

```


