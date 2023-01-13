
from flask import Flask, render_template
import pandas as pd
 
#*** Backend operation
# Read csv file in python_ flask
df = pd.read_csv('data/comment.csv')
 
# Read excel file in python_ flask
# df = pd.read_excel('data/comment.xlsx')
 
# WSGI Application
# Configure template folder name
# The default folder name should be "templates" else need to mention custom folder name for template path
# The default folder name for static files should be "static" else need to mention custom folder for static path
app = Flask(__name__, template_folder='templates', static_folder='static')
 
@app.route('/')
def index():
    return render_template('index_read_and_show_data.html')
 
@app.route('/show_data',  methods=("POST", "GET"))
def showData():
    # Convert pandas dataframe to html table flask
    df_html = df.to_html()
    return render_template('show_csv.html', data=df_html)
 
if __name__=='__main__':
    app.run(debug = True)