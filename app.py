from flask import Flask, redirect, request
app = Flask(__name__)
import json
import operations

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/insert", methods=["POST"])
def insert():
    print request.form
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    aes_enc = request.form["aes_enc"]
    ore_enc = request.form["ore_enc"]
    #pai_enc = request.form["pai_enc"]
    if operations.insert(first_name=first_name,last_name=last_name,aes_enc=aes_enc,ore_enc=ore_enc, pai_enc=None):
        id = operations.getID(aes_enc)
        dict = {"id":id}
        return json.dumps(dict)

if __name__ == "__main__":
    app.run()