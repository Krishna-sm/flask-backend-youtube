from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template('index.html')


# @app.route("/contact",methods=['GET','POST'])
# def hello2():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         mobile = request.form['mobile']
#         message = request.form['message']
#         message = request.form['message']
#         return render_template('index.html',msg="thanks for contact")
#     else :
#        return "hi this is krishna"


@app.route("/" ,methods=['POST'])
def hello():
    print(request.json['name'])
    return request.json


if __name__ == '__main__':
    app.run(debug=True)
