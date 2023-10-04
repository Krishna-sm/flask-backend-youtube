![Alt text](image.png)

# Templates  and HTML
- in the flask templates are keep in `templates folder` in root directory and access by render_template function
- all templates are treat as a `Jinja` template because we also use `jinja syntax` for dynamic data.


```python
  {{}} # access variable and url
  {%  %} # tags like for if and other

```

# for loop in template

```html

        {% for i in range(10) %}
      {{loop.index}}--  {{i}}
        {% endfor %}

```


# if statement in template

```html

       {% if names|length > 0 %}
            {% for i in names %}
            {{i}}
            {% endfor %}
            {% endif%}

```


# if statement in template

```html

       {% if names|length > 0 %}
            {% for i in names %}
            {{i}}
            {% endfor %}
            {% endif%}

```

# if else statement in template


```html
        {% if names|length < 0 %}
            {% for i in names %}
            {{i}}
            {% endfor %}
            {% else %}
            <h1>no such data found</h1>
            {% endif%}

```


# if elif else statement in template

```python

    
@app.route("/")
def helloworld():
    return render_template('index.html',name="Krishna")

app.run(debug=True)

```

```html
       {% if name=='Krishna' %}
        <h1>hy, krisna</h1>
        {% elif name=='radha' %}
        <h1>hy, radha</h1>
        {% else %}
        <h1>no name matched</h1>
        {% endif %}

```


# iterate dictonary

```python
    
@app.route("/")
def helloworld():
    return render_template('index.html',names={"name":"krishna","age":19})


```


```html
        {% for i in names %}
         {{names[i]}}
         {% endfor %}

```
# filters

[click Here](  https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters
)

```bash
  https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters

```



# Template Inheritence

syntax
```html
<!-- in layout file -->
<!-- for outleting the data -->
  {% block <name> %}
    {% endblock <name> %}
```

```html
        <!-- children file -->
        extends 'filename.html'

        {% block <name> %}
            <!-- render data  -->
        {% endblock <name> %}

```


example:

`templates/base.html`

```html
    <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}{%  endblock title %}</title>
 
  </head>
  <body>
            {% block body %}
            {% endblock body %}

 
  </body>
</html>

```



`templates/index.html`

```html
   {%  extends 'base.html' %}

{% block title %}
Home page
{% endblock title %}

{% block body %}
<h1>hi this is krishna</h1>
        {% endblock body%}

```


# Serve Static file

importing css/js/images files 

```html
           {{ url_for('static',filename='css/style.css')}}
           {{ url_for('static',filename='js/index.js')}}
           {{ url_for('static',filename='images/krishna.png')}}
           {{ url_for('static',filename='video/krishna.mp4')}}

```

## url 

```html
         <a href="{{url_for('github')}}">GO to github page</a>

```


