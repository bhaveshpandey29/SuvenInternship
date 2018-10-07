from flask import render_template,flash,url_for,redirect,Flask,session,logging,request
from wtforms import Form,StringField,TextAreaField,PasswordField,validators,form
import pandas as pd
from pandas import Series,DataFrame
import openpyxl
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

#data for forms

class SortingAction(Form):
    sourcefile = StringField('Source path and filename',[validators.Length(min = 1)])
    sheetname = StringField('Sheet Name',[validators.Length(min = 1)])
    colname = StringField('Column Name',[validators.Length(min = 1)])
    sortingorder = StringField('Sorting order',[validators.Length(min = 1)])
    newFile_dest = StringField('Destination path and filename',[validators.Length(min = 1)])
    newSheetName = StringField('Destination file sheetname',[validators.Length(min = 1)])  


@app.route('/start/',methods = ["POST","GET"])
def start():
    form = SortingAction(request.form)

    if request.method == 'POST' and form.validate():
        #fetching the data
        sourcefile = form.sourcefile.data
        sheetname = form.sheetname.data
        colname = form.colname.data
        sortingorder = form.sortingorder.data
        destfile = form.newFile_dest.data
        destfilesheet = form.newSheetName.data
        op_file = pd.read_excel(sourcefile,sheetname)
        sorted_data = op_file.sort_values(colname,ascending = (sortingorder)) ##Data sorted
        try:#trying to push data to new file
            sorted_data.to_excel(destfile,sheet_name = destfilesheet)
            my_file = Path(destfile)
            if(my_file.is_file):
                return render_template('finished.html/',form = form)
        except Exception as e:
            raise e
    return render_template('start.html',form = form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/finished')
def finished():
    return render_template('finished.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key' #secrent key init
    app.debug = True
    app.run()
