from flask import Flask, render_template, request, session,make_response,jsonify
from werkzeug.utils import secure_filename
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use("Agg")
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
	
@app.route('/index', methods=['GET','POST'])
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
   ex_mpt = mpt_data([mpt])
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
   ex_mpt = mpt_data([mpt])
   if mask == str(1):
      #print(ex_mpt.fast_mask())
      masked_mpt = mpt_data([data], mask = ex_mpt.fast_mask())
      #print(masked_mpt.df[0][['f','re','im']])
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(2):
      #print(ex_mpt.masker0())
      masked_mpt = mpt_data([data], mask = ex_mpt.masker0())
      #print(masked_mpt.df[0][['f','re','im']])
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(3):
      #print(ex_mpt.masker())
      masked_mpt = mpt_data([data], mask = ex_mpt.masker())
      #print(masked_mpt.df[0][['f','re','im']])
      df = masked_mpt.df[0][['f','re','im']]
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   elif mask == str(4):
      #print(ex_mpt.masker())
      masked_mpt = mpt_data([data])
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
      masked_mpt = mpt_data([data], mask = ex_mpt.fast_mask())
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
      masked_mpt = mpt_data([data], mask = ex_mpt.masker0())
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
      masked_mpt = mpt_data([data], mask = ex_mpt.masker())
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
      masked_mpt = mpt_data([data])
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
   data = mpt
   ex_mpt = mpt_data([mpt])
   re = []
   im = []

   if mask == str(1):
      masked_mpt = mpt_data([data], mask = ex_mpt.fast_mask())
      masked_mpt.guesser(no_of_fits=1)
      for i in masked_mpt.circuit_fit[0]:
         re.append(i.real)
         im.append(-i.imag)
      df_dict = {"REAL":re, "IMAGINARY":im}
      df = pd.DataFrame({'file':masked_mpt.data,
                     'fit_Rs':masked_mpt.fit_Rs,
                  "fit_R1":masked_mpt.fit_R1,
                  "fit_n1":masked_mpt.fit_n1,
                  "fit_Q1":masked_mpt.fit_Q1,                   
                  "fit_R2":masked_mpt.fit_R2,
                  "fit_n2":masked_mpt.fit_n2,
                  "fit_Q2":masked_mpt.fit_Q2,
                  "fit_Q3":masked_mpt.fit_Q,
                  "fit_n3":masked_mpt.fit_n,})
      return df
   elif mask == str(2):
      masked_mpt = mpt_data([data], mask = ex_mpt.masker0())
      masked_mpt.guesser(no_of_fits=500)
      for i in masked_mpt.circuit_fit[0]:
         re.append(i.real)
         im.append(-i.imag)
      df_dict = {"REAL":re, "IMAGINARY":im}
      df = pd.DataFrame({'file':masked_mpt.data,
                     'fit_Rs':masked_mpt.fit_Rs,
                  "fit_R1":masked_mpt.fit_R1,
                  "fit_n1":masked_mpt.fit_n1,
                  "fit_Q1":masked_mpt.fit_Q1,                   
                  "fit_R2":masked_mpt.fit_R2,
                  "fit_n2":masked_mpt.fit_n2,
                  "fit_Q2":masked_mpt.fit_Q2,
                  "fit_Q3":masked_mpt.fit_Q,
                  "fit_n3":masked_mpt.fit_n,})
      return df
   elif mask == str(3):
      masked_mpt = mpt_data([data], mask = ex_mpt.masker())
      masked_mpt.guesser(no_of_fits=500)
      for i in masked_mpt.circuit_fit[0]:
         re.append(i.real)
         im.append(-i.imag)
      df_dict = {"REAL":re, "IMAGINARY":im}
      df = pd.DataFrame({'file':masked_mpt.data,
                     'fit_Rs':masked_mpt.fit_Rs,
                  "fit_R1":masked_mpt.fit_R1,
                  "fit_n1":masked_mpt.fit_n1,
                  "fit_Q1":masked_mpt.fit_Q1,                   
                  "fit_R2":masked_mpt.fit_R2,
                  "fit_n2":masked_mpt.fit_n2,
                  "fit_Q2":masked_mpt.fit_Q2,
                  "fit_Q3":masked_mpt.fit_Q,
                  "fit_n3":masked_mpt.fit_n,})
      return df
   elif mask == str(4):
      masked_mpt = mpt_data([data])
      masked_mpt.guesser(no_of_fits=500)
      for i in masked_mpt.circuit_fit[0]:
         re.append(i.real)
         im.append(-i.imag)
      df_dict = {"REAL":re, "IMAGINARY":im}
      df = pd.DataFrame({'file':masked_mpt.data,
                     'fit_Rs':masked_mpt.fit_Rs,
                  "fit_R1":masked_mpt.fit_R1,
                  "fit_n1":masked_mpt.fit_n1,
                  "fit_Q1":masked_mpt.fit_Q1,                   
                  "fit_R2":masked_mpt.fit_R2,
                  "fit_n2":masked_mpt.fit_n2,
                  "fit_Q2":masked_mpt.fit_Q2,
                  "fit_Q3":masked_mpt.fit_Q,
                  "fit_n3":masked_mpt.fit_n,})
      return df
   else:
      return ("Error, not a Masking Function")

@app.route('/recal_mpt_guesser/<mpt>/<mask>/<bad_inds>')
def recal_mpt_guesser(mpt, mask,bad_inds):
   data = mpt
   ex_mpt = mpt_data([mpt])
   re = []
   im = []
   pre_inds = bad_inds.strip('][').split(',') 
   edited_inds = [int(i) for i in pre_inds]
   if mask == str(1):
      masked_mpt = mpt_data([data], mask = ex_mpt.fast_mask())
      for ind in edited_inds:
         if ind == "[":
            continue
         elif ind == "]":
            continue
         else:
            masked_mpt.df[0] = masked_mpt.df[0].drop(ind, axis = 0)
      masked_mpt.guesser(no_of_fits=1)
      for i in masked_mpt.circuit_fit[0]:
         re.append(i.real)
         im.append(-i.imag)
      df_dict = {"REAL":re, "IMAGINARY":im}
      df = pd.DataFrame.from_dict(df_dict)
      df = pd.DataFrame({'file':masked_mpt.data,
                     'fit_Rs':masked_mpt.fit_Rs,
                  "fit_R1":masked_mpt.fit_R1,
                  "fit_n1":masked_mpt.fit_n1,
                  "fit_Q1":masked_mpt.fit_Q1,                   
                  "fit_R2":masked_mpt.fit_R2,
                  "fit_n2":masked_mpt.fit_n2,
                  "fit_Q2":masked_mpt.fit_Q2,
                  "fit_Q3":masked_mpt.fit_Q,
                  "fit_n3":masked_mpt.fit_n,})
      return df
   elif mask == str(2):
      masked_mpt = mpt_data([data], mask = ex_mpt.masker0())
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
      df = pd.DataFrame({'file':masked_mpt.data,
                     'fit_Rs':masked_mpt.fit_Rs,
                  "fit_R1":masked_mpt.fit_R1,
                  "fit_n1":masked_mpt.fit_n1,
                  "fit_Q1":masked_mpt.fit_Q1,                   
                  "fit_R2":masked_mpt.fit_R2,
                  "fit_n2":masked_mpt.fit_n2,
                  "fit_Q2":masked_mpt.fit_Q2,
                  "fit_Q3":masked_mpt.fit_Q,
                  "fit_n3":masked_mpt.fit_n,})
      return df
   elif mask == str(3):
      masked_mpt = mpt_data([data], mask = ex_mpt.masker())
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
      df = pd.DataFrame({'file':masked_mpt.data,
                     'fit_Rs':masked_mpt.fit_Rs,
                  "fit_R1":masked_mpt.fit_R1,
                  "fit_n1":masked_mpt.fit_n1,
                  "fit_Q1":masked_mpt.fit_Q1,                   
                  "fit_R2":masked_mpt.fit_R2,
                  "fit_n2":masked_mpt.fit_n2,
                  "fit_Q2":masked_mpt.fit_Q2,
                  "fit_Q3":masked_mpt.fit_Q,
                  "fit_n3":masked_mpt.fit_n,})
      return df
   elif mask == str(4):
      masked_mpt = mpt_data([data])
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
      df = pd.DataFrame({'file':masked_mpt.data,
                     'fit_Rs':masked_mpt.fit_Rs,
                  "fit_R1":masked_mpt.fit_R1,
                  "fit_n1":masked_mpt.fit_n1,
                  "fit_Q1":masked_mpt.fit_Q1,                   
                  "fit_R2":masked_mpt.fit_R2,
                  "fit_n2":masked_mpt.fit_n2,
                  "fit_Q2":masked_mpt.fit_Q2,
                  "fit_Q3":masked_mpt.fit_Q,
                  "fit_n3":masked_mpt.fit_n,})
      return df
   else:
      return ("Error, not a Masking Function")

@app.route('/eisfitter/fit/<mpt>/<mask>/<bad_inds>')
def main_guesser(mpt, mask, bad_inds):
   if bad_inds == '[]':
      df = mask_mpt_guesser(mpt,mask)
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
   else:
      df = recal_mpt_guesser(mpt, mask,bad_inds)
      result = df.to_json(orient="index",indent = 2)
      return json.loads(result.replace('\\n', '\\\\n'))
  
@app.route('/eisfitter/fit')
def auto_guesser():
   dict_to_return = {}
   counter = 0
   for single_file in session['filenames']:
      counter += 1 
      to_add = {counter:main_guesser(single_file, '1', '[]')}
      dict_to_return.update(to_add)
   df = pd.DataFrame.from_dict(dict_to_return)
   result = df.to_json(orient="index",indent = 2)
   return json.loads(result.replace('\\n', '\\\\n'))
  

if __name__ == '__main__':
   app.secret_key = 'asdw34gegasdgf'
   app.run(debug = True)