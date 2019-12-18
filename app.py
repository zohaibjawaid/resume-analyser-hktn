"""
Created on March 2018

 █████╗ ██████╗  █████╗ ███╗   ███╗ █████╗ ███╗   ██╗████████╗██╗██╗   ██╗███╗   ███╗
██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔══██╗████╗  ██║╚══██╔══╝██║██║   ██║████╗ ████║
███████║██║  ██║███████║██╔████╔██║███████║██╔██╗ ██║   ██║   ██║██║   ██║██╔████╔██║
██╔══██║██║  ██║██╔══██║██║╚██╔╝██║██╔══██║██║╚██╗██║   ██║   ██║██║   ██║██║╚██╔╝██║
██║  ██║██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║   ██║   ██║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝     ╚═╝


"""

#################################################################################################################################################

import warnings
from flask import (Flask,render_template, request)

import util
import zipfile
import os

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

app = Flask(__name__)

app.config.from_object(__name__) # load config from this file , flaskr.py

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'docx', 'pdf'}

# class jd:
#     def __init__(self, name):
#         self.name = name
#
# def getfilepath(loc):
#     temp = str(loc).split('\\')
#     return temp[-1]
#


#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != app.config['USERNAME']:
#             error = 'Invalid username'
#         elif app.config['PASSWORD'] != hashlib.md5(request.form['password'].encode('utf-8')).hexdigest():
#             error = 'Invalid password'
#         else:
#             session['logged_in'] = True
#             flash('You were logged in')
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)
#
# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('You were logged out')
#     return redirect(url_for('home'))


@app.route('/')
def home():
    x = []
    # for file in glob.glob("./Job_Description/*.txt"):
    #     res = jd(file)
    #     x.append(jd(getfilepath(file)))
    # print(x)
    return render_template('index.html', result='some text', results=x)



#
# @app.route('/results', methods=['GET', 'POST'])
# def res():
#     if request.method == 'POST':
#         jobfile = request.form['des']
#         print(jobfile)
#         flask_return = screen.res(jobfile)
#
#         print(flask_return)
#         return render_template('result.html', results = flask_return)



# @app.route('/resultscreen' ,  methods = ['POST', 'GET'])
# def resultscreen():
#     if request.method == 'POST':
#         jobfile = request.form.get('Name')
#         print(jobfile)
#         flask_return = screen.res(jobfile)
#         return render_template('result.html', results = flask_return)



# @app.route('/resultsearch' ,methods = ['POST', 'GET'])
# def resultsearch():
#     if request.method == 'POST':
#         search_st = request.form.get('Name')
#         print(search_st)
#     result = search.res(search_st)
#     # return result
#     return render_template('result.html', results = result)


@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        folder = app.config['UPLOAD_FOLDER'] + 'single'
        f.save(os.path.join(folder, f.filename))
        characteristics = util.getCharacteristics(folder + '/' + f.filename)
        util.removeAllFilesFrom(folder)
        return render_template("single-result.html", result = characteristics)

@app.route('/bulk-upload', methods = ['POST'])
def bulkUpload():
    if request.method == 'POST':
        f = request.files['file']

        with zipfile.ZipFile(f, 'r') as zip_ref:
            zip_ref.extractall(app.config['UPLOAD_FOLDER'] + 'bulk')

        characteristics = util.getCharacteristics('asdf')

        return render_template("bulk-result.html", resumesData = [characteristics])


if __name__ == '__main__':
   # app.run(debug = True)
    # app.run('127.0.0.1' , 5000 , debug=True)
    app.run('0.0.0.0' , 5000 , debug=True , threaded=True)
    
