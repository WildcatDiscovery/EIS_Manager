from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
from tools import *
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['mpt'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


@app.route('/')
def welcome():
   return render_template('welcome_view.html')

@app.route('/upload')
def upload_file():
   return render_template('upload_view.html')
	
@app.route('/uploader', methods=['GET','POST'])
def upload():
   if request.method == "POST":
      uploaded_files = request.files.getlist("file[]")
      filenames = []
      for file in uploaded_files:
         if file and allowed_file(file.filename):
               filename = secure_filename(file.filename)
               file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
               filenames.append(filename)
      # This line is essential, store the data in session
      if session['filenames']:
         session['filenames'] = session['filenames'].extend(filenames)
         return render_template('result_view.html', filenames=session['filenames'])
      else:
         session['filenames'] = filenames
         return render_template('result_view.html', filenames=filenames)
   else:
      return render_template('result_view.html', filenames=session['filenames'])

@app.route('/displaydf/<mpt>', methods = ['GET', 'POST'])
def display_mpt(mpt):
   mpt = mpt_data(r"C:\Users\cjang.WILDCAT\Desktop\eis\eis_manager\data\\", [mpt])
   df = mpt.df_raw[['f', 're', 'im']]
   #mpt.mpt_plot(save_fig = "on")
   return render_template('dataframe_view.html', data = df.to_html(), df_head = (mpt.data))
		
if __name__ == '__main__':
   app.secret_key = 'asdw34gegasdgf'
   app.run(debug = True)