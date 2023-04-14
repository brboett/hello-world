from flask import Flask
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def hello_world():
    return "Test Application for OpenShift Dev Spaces - New Build"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
