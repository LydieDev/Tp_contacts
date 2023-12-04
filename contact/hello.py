from flask import Flask,render_template, request, redirect, flash,url_for
from app_blueprint import app_blueprint
from flask_mysqldb import MySQL

app= Flask(__name__)
app.secret_key="flash message"
app.register_blueprint(app_blueprint)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_contact'
 
mysql = MySQL(app)
@app.route("/", methods=['POST'])
def contact():
    product_data=request.form
    if request.method=="POST":
        flash("Data inserted successfully")
        nom=product_data['nom']
        desc=product_data['desc']
        num=product_data['num_phone']
        adresse=product_data['adresse']
        email=product_data['email']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO contact (nom,email,descript,adresse,num_phone) VALUES (%s,%s,%s,%s,%s)",(nom,email,desc,adresse,num))
        mysql.connection.commit()
        cursor.close()
        return render_template("contact.html")

@app.route('/data',methods=['GET','POST'])
def data():
    cur= mysql.connection.cursor()
    cur.execute("SELECT * FROM contact")
    data = cur.fetchall()
    cur.close()
    return render_template("data.html",data=data)