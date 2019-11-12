from flask import Flask, render_template, redirect, jsonify
from bson.json_util import loads, dumps
#Local imports

app = Flask(__name__)

@app.route("/")
def home():
    #Get mars dict
    ##data_webpage = charts.consult_snap_db()
    ##data_webpage = dumps(data_webpage)
    #Return template and data
    #return render_template("index.html", data_app=data_webpage)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)