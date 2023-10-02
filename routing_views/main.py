from flask import Flask,render_template,jsonify,request

krishna = Flask(__name__)

@krishna.route("/")
def greet():
    name = request.args.get("name")
    age = request.args.get("age")
    # name ="hari"
    return render_template('index.html',name=name,age=age),201

@krishna.route("/krishna/<string:name>/<float:id>")
def greetsh(name,id):
    print(type(name))
    print(type(id))
    return jsonify({"name":name,"age":id}),404

@krishna.errorhandler(404)
def not_found(eror):
    print(eror)
    return render_template('404.html'),404

if __name__ == '__main__':
    krishna.run(debug=True)