import requests
import re
import base64
import os
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import Model, ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, flash
import dotenv
dotenv.load_dotenv()
api_key = os.getenv("WATSONX_APIKEY")
model_id = "meta-llama/llama-4-maverick-17b-128e-instruct-fp8"
app = Flask(__name__)

### You will add code from Step 2 here
credentials = Credentials(
            url="https://eu-de.ml.cloud.ibm.com",
            api_key=api_key
        )

### Step 3

### Step 4

### Step 5

@app.route('/generate', methods=['POST'])
def index():
    # This is where you'll add your main application logic later, after step 5
    #TODO
    pass

if __name__ == '__main__':
    app.run(debug=True)