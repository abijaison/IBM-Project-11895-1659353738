from flask import Flask,render_template,request,redirect,session
import sqlite3 as sql

app = Flask(__name__,template_folder='templates')
app.secret_key = 'fasdgfdgdfg'


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/addstudent')
def new_student():
   return render_template('add_student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         addr = request.form['address']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("students.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(name,addr,city,pin) )
            con.commit()
            msg = "Record successfully added!"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("list.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("students.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   students = cur.fetchall();
   return render_template("list.html", students = students)
@app.route('/signup',methods=['POST','GET'])
def signup():
   if request.method == 'POST':

      name = request.form['name']
      email = request.form['email']
      phone= request.form['phone']
      password= request.form['password']
         
      with sql.connect("users.db") as con:
          cur = con.cursor()
          cur.execute("INSERT INTO users (name,email,phoneno,password) VALUES (?,?,?,?)",(name,email,phone,password) )
          con.commit()
          msg = "Record successfully added!"
   con = sql.connect("users.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from users")
   users = cur.fetchall();
   return render_template("signup.html",users=users)

if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0')
