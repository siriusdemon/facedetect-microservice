from flask import Flask, request
import json
import centerface
from PIL import Image


app = Flask(__name__)

@app.route("/", methods=['POST'])
def detect():
    img = request.files['image']
    img = Image.open(img)
    result = centerface.detect(img)
    return {"result": result}

