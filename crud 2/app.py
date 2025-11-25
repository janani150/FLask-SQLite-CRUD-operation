from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

app.secret_key = 'admin456'

@app.route("/")
@app.route("/index")
def index():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    con.close()
    return render_template("index.html", datas=data)

@app.route("/add_user", methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        uname = request.form['uname']
        contact = request.form['contact']
        address = request.form['address']
        email = request.form['email']
        age = request.form['age']
        
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users (UNAME, CONTACT, address, email, age) VALUES (?, ?, ?, ?, ?)",
                    (uname, contact, address, email, age))
        con.commit()
        con.close()
        flash('User Added', 'success')
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:uid>", methods=['POST', 'GET'])
def edit_user(uid):
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    
    if request.method == 'POST':
        uname = request.form['uname']
        contact = request.form['contact']
        address = request.form['address']
        email = request.form['email']
        age = request.form['age']
        
        cur.execute("UPDATE users SET UNAME=?, CONTACT=?, address=?, email=?, age=? WHERE UID=?",
                    (uname, contact, address, email, age, uid))
        con.commit()
        con.close()
        flash('User Updated', 'success')
        return redirect(url_for("index"))
    
    cur.execute("SELECT * FROM users WHERE UID=?", (uid,))
    data = cur.fetchone()
    con.close()
    return render_template("edit_user.html", datas=data)

@app.route("/delete_user/<string:uid>", methods=['GET'])
def delete_user(uid):
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE UID=?", (uid,))
    con.commit()
    con.close()
    flash('User Deleted', 'warning')
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
