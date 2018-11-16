from flask import Flask
app = Flask(__name__)

# Set application configs
app.config['API_ENDPOINT'] = "https://api.ciliar.co/v1/image"
app.config['API_AUTH_KEY'] = ""
app.config['BASE_IMG'] = 'http://speedhunters-wp-production.s3.amazonaws.com/wp-content/uploads/2013/12/01124507/paul-walker-RIP-2-1200x799.jpg'
app.config['LABEL_CSS'] = ['label-default','label-primary','label-success','label-info','label-warning']

import workflow.views