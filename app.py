from flask import Flask, render_template,request,flash,redirect,url_for
import sqlite3
import sqlite3 as sql
import datetime
from twilio import twiml

app = Flask(__name__)
app.secret_key="123"

#con=sqlite3.connect("database.db")
#con.execute("CREATE TABLE IF NOT EXISTS data(pid INTEGER PRIMARY KEY ,name TEXT,address TEXT,contact INTEGER,mail TEXT)")
#con.close()

@app.route('/')
def home():
    return ("Hello World")

@app.route('/LosAngelesSMS')
def LosAngelesSMS():
    return render_template('LosAngelesSMS.html')

@app.route('/SeattleSMS')
def SeattleSMS():
    return render_template('SeattleSMS.html')

@app.route('/TexasSMS')
def TexasSMS():
    return render_template('TexasSMS.html')

@app.route('/EcostarLA',methods=["POST","GET"])
def EcostarLA():
    if request.method=="POST":
            number = request.form['From']
            text = request.form['Body']
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            if number:
                with sql.connect("databaseLA.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO data (date,number,text) VALUES (?,?,?)",(date,number,text))
                return "Number:{} Text:{}".format(number, text)
            if not number:
                return "No Data"
    else:
                  con=sqlite3.connect("database.db")
                  con.row_factory=sqlite3.Row
                  cur=con.cursor()
                  cur.execute("SELECT * from data")
                  data=cur.fetchall()
                  con.close()
                  return render_template("EcostarLA.html",data=data)

@app.route("/EcostarTX",methods=["GET","POST"])
def EcostarTX():
    if request.method=="POST":
            number = request.form['From']
            text = request.form['Body']
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            if number:
                with sql.connect("databaseTX.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO data (date,number,text) VALUES (?,?,?)",(date,number,text))
                return "Number:{} Text:{}".format(number, text)
            if not number:
                return "No Data"
    else:
                  con=sqlite3.connect("databaseTX.db")
                  con.row_factory=sqlite3.Row
                  cur=con.cursor()
                  cur.execute("SELECT * from data")
                  data=cur.fetchall()
                  con.close()
                  return render_template("EcostarTX.html",data=data)

@app.route("/EcostarSea",methods=["GET","POST"])
def EcostarSea():
    if request.method=="POST":
            number = request.form['From']
            text = request.form['Body']
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            if number:
                with sql.connect("databaseWA.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO data (date,number,text) VALUES (?,?,?)",(date,number,text))
                return "Number:{} Text:{}".format(number, text)
            if not number:
                return "No Data"
    else:
                  con=sqlite3.connect("databaseWA.db")
                  con.row_factory=sqlite3.Row
                  cur=con.cursor()
                  cur.execute("SELECT * from data")
                  data=cur.fetchall()
                  con.close()
                  return render_template("EcostarSea.html",data=data)

@app.route('/delete_record/<string:id>')
def delete_record(id):
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
    finally:
        return redirect(url_for("EcostarLA"))
        con.close()    

@app.route('/delete_record2/<string:id>')
def delete_record2(id):
    try:
        con = sqlite3.connect("databaseTX.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
    finally:
        return redirect(url_for("EcostarTX"))
        con.close()    

@app.route('/delete_record3/<string:id>')
def delete_record3(id):
    try:
        con = sqlite3.connect("databaseWA.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
    finally:
        return redirect(url_for("EcostarSea"))
        con.close()  

if __name__ == "__main__":
    app.run(debug=True) 