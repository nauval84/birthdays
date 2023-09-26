import os #import os untuk mengakses sistem database

from cs50 import SQL #import SQL untuk menggunakan bahasa SQL dalam phyton

from flask import Flask, flash, jsonify, redirect, render_template, request, session #import tools untuk website

app = Flask(__name__) #mengatur nama aplikasi

db = SQL ("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
#ketika route "/" dipanggil/diakses, maka fungsi inde() dieksekusi
def index():
    #jika requst yang dilakukan oleh pungguna adalah post, maka eksekusi kode dalam if 
    if request.method == "POST":
        #access form data / membaca data pada yang diisikan pada form 
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day") 

        #masukkan data ke database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        #balik ke https://127.0.0.1:5000/
        return redirect("/")
        
    # jika requestnya selain post, maka tampilkan data dari tabel birthdays  
    else:
        # ambil seluruh data dari tabel birthdays, simpan di variabel birthdays
        birthdays = db.execute("SELECT * FROM birthdays")

        # salin isi variabel birtdays ke birhdays, lalu kirim ke index.html
        return render_template("index.html", birthdays =birthdays) 