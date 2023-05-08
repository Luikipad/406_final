from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
   return render_template('home.htm')

@app.route('/enternew')
def new_student():
   return render_template('client.htm')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         ClientID = request.form['ClientID']
         ClientName = request.form['ClientName']
         ClientPhone = request.form['ClientPhone']
         ClientWatch = request.form['ClientWatch']
         TotalSpent = request.form['TotalSpent']
         
         with sql.connect(host="localhost", user="flask", password="password", database="flask_db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO employee (ClientID,ClientName,ClientPhone,ClientWatch,TotalSpent) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(ClientID,ClientName,ClientPhone,ClientWatch,TotalSpent)
            cur.execute(cmd)
            
            con.commit()
            msg = "Successfully Added Record to Database!"
      except:
         con.rollback()
         msg = "Error, please try again."
         
      finally:
         return render_template("output.htm",msg = msg)
         con.close()

@app.route('/list')
def list():
   with sql.connect(host="localhost", user="flask", password="password", database="client_db") as conn:  
      cur = conn.cursor()
      cur.execute("select * from client")
      rows = cur.fetchall()

   return render_template("list.htm",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)