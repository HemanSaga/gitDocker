from flask import Flask 
app = Flask(__name__)
@app.route("/")
def home():
    return "The git is integrated with the docker for proper version controll of the programming files"
if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000)