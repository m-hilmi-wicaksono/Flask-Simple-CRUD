
from flask import Flask, render_template, request, url_for, redirect
from flask_mysql_connector import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'toor01'
app.config['MYSQL_DB'] = 'flaskdb'
mysql = MySQL(app)
nama_db = 'use flaskdb'

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute(nama_db)
    cur.execute("SELECT * FROM computer")
    rv = cur.fetchall()
    cur.close()
    return render_template('home.html', computers=rv)


@app.route('/about-us')
def aboutUs():
    return render_template('about-us.html')

@app.route('/contact-us')
def contactUs():
    return render_template('contact-us.html')

@app.route('/simpan',methods=["POST"])
def simpan():
    nama = request.form['nama']
    cur = mysql.connection.cursor()
    cur.execute(nama_db)
    cur.execute("INSERT INTO computer (data) VALUES (%s)",(nama,))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    nama = request.form['nama']
    cur = mysql.connection.cursor()
    cur.execute(nama_db)
    cur.execute("UPDATE computer SET data=%s WHERE id=%s", (nama,id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute(nama_db)
    cur.execute("DELETE FROM computer WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=False)