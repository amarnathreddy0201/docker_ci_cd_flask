from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    return render_template("index.html")


if __name__=="__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0",port=8080)