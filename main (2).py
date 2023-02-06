from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route("/")

def homepage():
    return "This is Home Page"

@app.route("/add",methods=["POST"])
def addition():
    #if request.method=="POST": # dont need to define twice, works either way
        result = int(request.json["num1"]) + (request.json["num2"])
        return jsonify("The operation is addition and result is {}".format(result))

if __name__=="__main__":
    app.run(host="0.0.0.0",port = 5001)