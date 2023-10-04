from flask import Flask,render_template

app = Flask(__name__,template_folder='krishna',static_folder='public')

@app.route("/")
def hello():
    # num=19
    return render_template('index.html')

@app.route("/about")
def hello2():
    # num=19
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)