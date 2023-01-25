from flask import Flask, render_template, request, session
import pandas as pd
import os
from werkzeug.utils import secure_filename
    
app = Flask(__name__, template_folder='templates', static_folder='static')
 
@app.route('/')
def index():
    return "<h1>Let's get this shit done</h1>"
    # text="Upload any csv file"
    # return render_template('index.html',text1=text)




if __name__=='__main__':
    app.run(debug = True)