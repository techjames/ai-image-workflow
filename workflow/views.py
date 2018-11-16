
import requests
import json
import random
from datetime import datetime
from flask import render_template
from flask import request
from workflow import app

@app.route('/', methods=['GET', 'POST'])
def home():
    imglink = app.config['BASE_IMG']
    images = []

    if request.method == 'POST':
        imglink=request.form.get('imglink')
    else:
        imglink = app.config['BASE_IMG']


    headers = {'Authorization': app.config['API_AUTH_KEY'], 'Content-Type': "application/json", 'accept': "application/json"}
    payload = {'url': imglink}

    response = requests.post(app.config['API_ENDPOINT'], headers=headers, data=json.dumps(payload), verify=False)
    print(response.json())
    response_data = response.json()

    class Image:
        def __init__(self, label, left, top, confidence):
            self.label = label
            self.left = left
            self.top = top
            self.label_css = random.choice(app.config['LABEL_CSS'])
            self.confidence = confidence


    for i in range(len(response_data["boxes"])):
        label = response_data["boxes"][i]["label"]
        left = response_data["boxes"][i]["left"] / (response_data["width"] / 636)
        top = response_data["boxes"][i]["top"] / (response_data["height"] / 340)
        confidence = response_data["boxes"][i]["confidence"] * 100
            
        image = Image(label, left, top, confidence)
        images.append(image)


    return render_template(
        'layout.html',
         title='(AI) Image Workflow',
         imglink=imglink,
         images=images
    )


