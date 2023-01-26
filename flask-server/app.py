from flask import Flask, render_template, request, session,jsonify
import pandas as pd
from io import BytesIO
from werkzeug.utils import secure_filename


    
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










    response=""
    return response

if __name__=='__main__':
    app.run(debug = True)