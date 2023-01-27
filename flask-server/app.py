from flask import Flask, render_template, request, session,jsonify
import pandas as pd
from io import BytesIO
from werkzeug.utils import secure_filename
from utils.preprocessing import *
import json

import numpy as np
import pandas as pd
import re
import nltk
import spacy
import string
pd.options.mode.chained_assignment = None
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import json
from collections import Counter

with open('/utils/abbreviations.json') as json_file:
    abbreviations = json.load(json_file)
PUNCT_TO_REMOVE = string.punctuation
", ".join(stopwords.words('english'))
FREQWORDS = set([w for (w, wc) in cnt.most_common(10)])


app = Flask(__name__)
 
@app.route('/data')
def data():
    return {"Flask Server":"Pratham"}
    # text="Upload any csv file"
    # return render_template('index.html',text1=text)
    
@app.route("/",methods=["POST"])
def return_csv():
    d=request.file
    print(d)

@app.route('/upload', methods=['POST'])
def fileUpload():
    file = request.files['file'] 
    filename = file.filename
    file_bytes = file.read()
    file_content = BytesIO(file_bytes).readlines()
    train=pd.DataFrame(file_content)
    shape=train.shape[1]
    train.columns=['col'+str(i) for i in range(shape)]
    columns_to_exclude=list((train.select_dtypes(exclude=['object'])).columns)
    columns=list((train.select_dtypes(include=['object'])).columns)
    
    res=train[columns_to_exclude]
    train=train[columns]


    for col in columns:
        train[col]=train[col].astype(str)
        train[col]=train[col].str.lower()







    response=""
    return response

if __name__=='__main__':
    app.run(debug = True)

