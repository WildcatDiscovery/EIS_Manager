from flask import Flask, render_template, request, session,make_response,jsonify
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from tools import *
import os
import io
import json
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['mpt'])
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

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


@app.route('/display_mpt/<mpt>', methods = ['GET', 'POST'])
def display_mpt(mpt):
   ex_mpt = mpt_data(r"C:\Users\cjang.WILDCAT\Desktop\eis\eis_manager\data\\", [mpt])
   df = ex_mpt.df_raw[['f', 're', 'im']]
   result = df.to_json(orient="index",indent = 2)
   return json.loads(result.replace('\\n', '\\\\n'))

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

@app.route('/mask_mpt/<mpt>/<mask>')
def mask_mpt(mpt, mask):
   path = r"C:\Users\cjang.WILDCAT\Desktop\eis\eis_manager\data\\"
   data = mpt
   ex_mpt = mpt_data(path, [mpt])
   if mask == str(1):
      #print(ex_mpt.fast_mask())
      masked_mpt = mpt_data(path, [data], mask = ex_mpt.fast_mask())
      #print(masked_mpt.df[0][['f','re','im']])
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(2):
      #print(ex_mpt.masker0())
      masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker0())
      #print(masked_mpt.df[0][['f','re','im']])
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(3):
      #print(ex_mpt.masker())
      masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker())
      #print(masked_mpt.df[0][['f','re','im']])
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(4):
      #print(ex_mpt.masker())
      masked_mpt = mpt_data(path, [data])
      #print(masked_mpt.df[0][['f','re','im']])
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   else:
      return ("Error, not a Masking Function")

@app.route('/recal_mpt/<mpt>/<mask>/<bad_inds>')
def recal_mpt(mpt, mask, bad_inds):
   path = r"C:\Users\cjang.WILDCAT\Desktop\eis\eis_manager\data\\"
   data = mpt
   ex_mpt = mpt_data(path, [mpt])
   pre_inds = bad_inds.strip('][').split(',') 
   edited_inds = [int(i) for i in pre_inds]
   if mask == str(1):
      masked_mpt = mpt_data(path, [data], mask = ex_mpt.fast_mask())
      for ind in edited_inds:
        if ind == "[":
            continue
        elif ind == "]":
            continue
        else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(2):
      #print(ex_mpt.masker0())
      masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker0())
      for ind in edited_inds:
        if ind == "[":
            continue
        elif ind == "]":
            continue
        else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(3):
      #print(ex_mpt.masker())
      masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker())
      for ind in edited_inds:
        if ind == "[":
            continue
        elif ind == "]":
            continue
        else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(4):
      #print(ex_mpt.masker())
      masked_mpt = mpt_data(path, [data])
      for ind in edited_inds:
        if ind == "[":
            continue
        elif ind == "]":
            continue
        else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   else:
      return ("Error, not a Masking Function")
   
@app.route('/mask_mpt_guesser/<mpt>/<mask>')
def mask_mpt_guesser(mpt, mask):
   path = r"C:\Users\cjang.WILDCAT\Desktop\eis\eis_manager\data\\"
   data = mpt
   ex_mpt = mpt_data(path, [mpt])
   re = []
   im = []
   if mpt in session:
      return session[mpt]
   else:
      if mask == str(1):
         masked_mpt = mpt_data(path, [data], mask = ex_mpt.fast_mask())
         masked_mpt.guesser(no_of_fits=500)
         for i in masked_mpt.circuit_fit[0]:
            re.append(i.real)
            im.append(-i.imag)
         df_dict = {"REAL":re, "IMAGINARY":im}
         df = pd.DataFrame.from_dict(df_dict)
         result = df.to_json(orient="index",indent = 2)
         session[masked_mpt.data[0]] = json.loads(result.replace('\\n', '\\\\n'))
         return json.loads(result.replace('\\n', '\\\\n'))
      elif mask == str(2):
         masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker0())
         masked_mpt.guesser(no_of_fits=500)
         for i in masked_mpt.circuit_fit[0]:
            re.append(i.real)
            im.append(-i.imag)
         df_dict = {"REAL":re, "IMAGINARY":im}
         df = pd.DataFrame.from_dict(df_dict)
         result = df.to_json(orient="index",indent = 2)
         session[masked_mpt.data[0]] = json.loads(result.replace('\\n', '\\\\n'))
         return json.loads(result.replace('\\n', '\\\\n'))
      elif mask == str(3):
         masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker())
         masked_mpt.guesser(no_of_fits=500)
         for i in masked_mpt.circuit_fit[0]:
            re.append(i.real)
            im.append(-i.imag)
         df_dict = {"REAL":re, "IMAGINARY":im}
         df = pd.DataFrame.from_dict(df_dict)
         result = df.to_json(orient="index",indent = 2)
         session[masked_mpt.data[0]] = json.loads(result.replace('\\n', '\\\\n'))
         return json.loads(result.replace('\\n', '\\\\n'))
      elif mask == str(4):
         masked_mpt = mpt_data(path, [data])
         masked_mpt.guesser(no_of_fits=500)
         for i in masked_mpt.circuit_fit[0]:
            re.append(i.real)
            im.append(-i.imag)
         df_dict = {"REAL":re, "IMAGINARY":im}
         df = pd.DataFrame.from_dict(df_dict)
         result = df.to_json(orient="index",indent = 2)
         session[masked_mpt.data[0]] = json.loads(result.replace('\\n', '\\\\n'))
         return json.loads(result.replace('\\n', '\\\\n'))
      else:
         return ("Error, not a Masking Function")

@app.route('/recal_mpt_guesser/<mpt>/<mask>/<bad_inds>')
def recal_mpt_guesser(mpt, mask,bad_inds):
   path = r"C:\Users\cjang.WILDCAT\Desktop\eis\eis_manager\data\\"
   data = mpt
   ex_mpt = mpt_data(path, [mpt])
   re = []
   im = []
   pre_inds = bad_inds.strip('][').split(',') 
   edited_inds = [int(i) for i in pre_inds]
   if mask == str(1):
      masked_mpt = mpt_data(path, [data], mask = ex_mpt.fast_mask())
      for ind in edited_inds:
         if ind == "[":
            continue
         elif ind == "]":
            continue
         else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
      masked_mpt.guesser(no_of_fits=500)
      for i in masked_mpt.circuit_fit[0]:
         re.append(i.real)
         im.append(-i.imag)
      df_dict = {"REAL":re, "IMAGINARY":im}
      df = pd.DataFrame.from_dict(df_dict)
      result = df.to_json(orient="index",indent = 2)
      session[masked_mpt.data[0]] = json.loads(result.replace('\\n', '\\\\n'))
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(2):
      masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker0())
      for ind in edited_inds:
         if ind == "[":
            continue
         elif ind == "]":
            continue
         else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
      masked_mpt.guesser(no_of_fits=500)
      for i in masked_mpt.circuit_fit[0]:
         re.append(i.real)
         im.append(-i.imag)
      df_dict = {"REAL":re, "IMAGINARY":im}
      df = pd.DataFrame.from_dict(df_dict)
      result = df.to_json(orient="index",indent = 2)
      session[masked_mpt.data[0]] = json.loads(result.replace('\\n', '\\\\n'))
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(3):
      masked_mpt = mpt_data(path, [data], mask = ex_mpt.masker())
      for ind in edited_inds:
         if ind == "[":
            continue
         elif ind == "]":
            continue
         else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
      masked_mpt.guesser(no_of_fits=500)
      for i in masked_mpt.circuit_fit[0]:
         re.append(i.real)
         im.append(-i.imag)
      df_dict = {"REAL":re, "IMAGINARY":im}
      df = pd.DataFrame.from_dict(df_dict)
      result = df.to_json(orient="index",indent = 2)
      session[masked_mpt.data[0]] = json.loads(result.replace('\\n', '\\\\n'))
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(4):
      masked_mpt = mpt_data(path, [data])
      for ind in edited_inds:
         if ind == "[":
            continue
         elif ind == "]":
            continue
         else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
      masked_mpt.guesser(no_of_fits=500)
      for i in masked_mpt.circuit_fit[0]:
         re.append(i.real)
         im.append(-i.imag)
      df_dict = {"REAL":re, "IMAGINARY":im}
      df = pd.DataFrame.from_dict(df_dict)
      result = df.to_json(orient="index",indent = 2)
      session[masked_mpt.data[0]] = json.loads(result.replace('\\n', '\\\\n'))
      return json.loads(result.replace('\\n', '\\\\n'))
   else:
      return ("Error, not a Masking Function")

if __name__ == '__main__':
   app.secret_key = 'asdw34gegasdgf'
   app.run(debug = True)