from flask import Flask, redirect, url_for, render_template, jsonify, request
import mysql.connector as sql
import sqlalchemy

mydb=sql.connect(host="localhost", user="root", password="951753", database="apexdata")
mycursor=mydb.cursor()
app=Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        wr=request.form["wname"]
        return redirect(url_for("search", name=wr))
    else:
        return render_template("index.html")

@app.route("/weapons", methods=["POST", "GET"])
def weapons():
    mycursor.execute("""SELECT id, name, type, ammo FROM weapons""")
    wdb=mycursor.fetchall()
    tlb = ["ID","Name","Type","Ammo"]
    p=[]
    for row in wdb:
        k=[]
        a = "%s"%row[0]
        k.append(a)
        b = "%s"%row[1]
        k.append(b)
        c = "%s"%row[2]
        k.append(c)
        d = "%s"%row[3]
        k.append(d)
        p.append(k)
    return render_template("weapons.html",col=tlb, p=p)

@app.route("/weapons/search", methods=["POST", "GET"])
def Search():
    bs=request.form["wname"]
    mycursor.execute(f"SELECT * FROM weapons WHERE name LIKE '%{bs}%' ")
    sr=mycursor.fetchall()
    tlb1 = ["ID","Name","Type","Ammo","Body damage", "Head damage", "Leg damage","Mag size","RPM", "DPS","TTK", "Projectile Speed", "Fire Modes" ]
    p1=[]
    for row1 in sr:
        k1=[]
        a1 = "%s"%row1[0]
        k1.append(a1)
        b1 = "%s"%row1[1]
        k1.append(b1)
        c1 = "%s"%row1[2]
        k1.append(c1)
        d1 = "%s"%row1[3]
        k1.append(d1)
        e = "%s"%row1[4]
        k1.append(e)
        f = "%s"%row1[5]
        k1.append(f)
        g = "%s"%row1[6]
        k1.append(g)
        h = "%s"%row1[7]
        k1.append(h)
        i = "%s"%row1[8]
        k1.append(i)
        j = "%s"%row1[9]
        k1.append(j)
        m = "%s"%row1[10]
        k1.append(m)
        n = "%s"%row1[11]
        k1.append(n)
        o = "%s"%row1[12]
        k1.append(o)
        p1.append(k1)
    return render_template("search.html",col1=tlb1, p1=p1)
