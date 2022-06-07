from flask import render_template
from flask import Flask
from datetime import datetime
import re
import os,json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    # with open('static\data.json') as file:
    #     data = json.load(file)
    # random_text = data["penyu"][1]["nama"]
    return render_template(
        "about.html",
        # random_text = random_text
    )


@app.route("/penyu/tes")
def penyu():
    data = []
    with open('static\data.json') as file:
        data = json.load(file)
        print(data)
        # for i in data:
        #     nama = i["nama"]
        #     nama_latin = i["nama_latin"]
        #     deskripsi = i["deskripsi"]
        return render_template(    
            "penyu.html",
            penyu = data
            # nama = nama ,
            # nama_latin = nama_latin,
            # deskripsi = deskripsi,
    )

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello.html",
        name=name,
        date=datetime.now()
    )


    
if __name__ == "__main__":
    app.run(debug=True)