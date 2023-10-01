From flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello_world():
    return "Hi, Krishna"

if __name__ == '__main__':
    app.run(debug=True)
