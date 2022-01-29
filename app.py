from flask import Flask
from flask import render_template
from flask import request

import datetime

app = Flask(__name__)

entries = []

@app.route("/", methods=['GET','POST'])
def home_f():
    if request.method == "POST":
        entry_content=request.form['content']
        formatted_date = datetime.datetime.today().strftime("%d-%m-%Y")
        entries.append([entry_content,formatted_date])
    entries_with_date=[
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1],"%d-%m-%Y").strftime("%b %d")
        ) for entry in entries
    ]
    return render_template('home.html',entries=entries_with_date)