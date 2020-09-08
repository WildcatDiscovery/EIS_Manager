from flask import Flask, render_template, request, session,make_response
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from tools import *
import os
import io
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
      session['filenames'] = filenames
      return render_template('result_view.html', filenames=filenames)
   else:
      return render_template('result_view.html', filenames=session['filenames'])

@app.route('/displaydf/<mpt>', methods = ['GET', 'POST'])
def display_mpt(mpt):
   ex_mpt = mpt_data(r"C:\Users\cjang.WILDCAT\Desktop\eis\eis_manager\data\\", [mpt])
   df = ex_mpt.df_raw[['f', 're', 'im']]
   #plot(df['re'], df['im'])
   #return plot(df['re'], df['im'], mpt.data[0])
   return render_template('dataframe_view.html', data = df.to_html(), df_head = (ex_mpt.data), file = ex_mpt.data[0])


@app.route('/plot_mpt/<mpt>')
def plot(mpt):
   ex_mpt = mpt_data(r"C:\Users\cjang.WILDCAT\Desktop\eis\eis_manager\data\\", [mpt])
   xs = ex_mpt.df_raw['re']
   ys = ex_mpt.df_raw['im']
   title = ex_mpt.data[0]
   fig = Figure(dpi=120, figsize = [15, 25], facecolor='w', edgecolor='w')
   fig.subplots_adjust(left=0.1, right=0.95, hspace=0.5, bottom=0.1, top=0.95)
   ax = fig.add_subplot(211, aspect='equal')
   ax.set_xlabel('Re(Z)/Ohm')
   ax.set_ylabel('-Im(Z)/Ohm')
   ax.plot(xs, ys, marker='o', ms=4, lw=2, ls='-', label = "Nvyquist Impedance Data")
   ax.legend()
   ax.set_title(title)
    #fig = Figure()
    #axis = fig.add_subplot(1, 1, 1)
    #axis.plot(xs, ys, '.')
   canvas = FigureCanvas(fig)
   output = io.BytesIO()
   canvas.print_png(output)
   response = make_response(output.getvalue())
   response.mimetype = 'image/png'
   return response

if __name__ == '__main__':
   app.secret_key = 'asdw34gegasdgf'
   app.run(debug = True)