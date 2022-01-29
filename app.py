from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from pymongo import MongoClient
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app_db=client.Microblog
    # entries = [] 

    @app.route("/", methods=['GET','POST'])
    def home_f():
        # print([e for e in app_db.Entries.find({})])
        if request.method == "POST":
            entry_content=request.form['content']
            formatted_date = datetime.datetime.today().strftime("%d-%m-%Y")
            app_db.Entries.insert_one({"content":entry_content,"date":formatted_date})
            return redirect(url_for('home_f'))
        #     entries.append([entry_content,formatted_date])
        # entries_with_date=[
        #     (
        #         entry[0],
        #         entry[1],
        #         datetime.datetime.strptime(entry[1],"%d-%m-%Y").strftime("%b %d")
        #     ) for entry in entries
        # ]
        
        entries_with_date=[
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"],"%d-%m-%Y").strftime("%b %d")
            ) for entry in app_db.Entries.find({})
            ]
        
        return render_template('home.html',entries=entries_with_date)
    
    return app
