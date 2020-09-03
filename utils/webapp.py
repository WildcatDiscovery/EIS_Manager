from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)
from tools import *

import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

@app.route('/')
def welcome():
   return render_template('welcome.html')

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_filer():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      df = mpt_data(r"C:\Users\cjang.WILDCAT\Desktop\eis\eis_manager\data\\", [f.filename]).df_raw[['f', 're', 'im']]
      return render_template('result.html',  tables=[df.to_html(classes='data')], titles=df.columns.values, df_head = str(f.filename))
		
if __name__ == '__main__':
   app.run(debug = True)