from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file

application = Flask(__name__)

import rds_db as db

@application.route('/')
def index():
    
    details = db.get_details()
    print(details)
    #for detail in details:
    #    var = detail
    return render_template('index.html',var=details)

@application.route('/insert',methods = ['post'])
def insert():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['optradio']
        comment = request.form['comment']
        db.insert_details(name,email,comment,gender)
        details = db.get_details()
        print(details)
        for detail in details:
            var = detail
        return render_template('index.html',var=var)



if __name__ == "__main__":
    
    application.run(host='0.0.0.0',debug=True)
#application.run(host='0.0.0.0',debug=True)
#application.run(host='0.0.0.0',debug=True,use_reloader=False)
