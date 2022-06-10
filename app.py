from flask import render_template
from flask import Flask
from datetime import datetime
import re
import pickle
import os,json
import numpy as np
import cv2

model = pickle.load(open('VGG-16.ipynb','rb'))

app = Flask(__name__)



ML_MODEL_FILE = "VGG-16.ipynb"

def imdecode_image(image_file):
    return cv2.imdecode(
        np.frombuffer(image_file.read(), np.uint8),
        cv2.IMREAD_UNCHANGED
    )

# def recognize_turtles_by_cv_image(cv_image):
    # freshness_percentage = freshness_percentage_by_cv_image(cv_image)
    # return {
    #     # TODO: change freshness_level to freshness_percentage
    #     "freshness_level": freshness_percentage,
    #     "price": price_by_freshness_percentage(freshness_percentage)
    # }

@app.route("/")
def home():
    return render_template("home.html")



@app.route('/api/recognize', methods=["POST"])
def api_recognize():
    cv_image = imdecode_image(request.files["image"])
    return recognize_turtles_by_cv_image(cv_image)

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