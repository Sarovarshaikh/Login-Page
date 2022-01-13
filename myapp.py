from flask import *
from DBM import *
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/unsucc")
def unsuccessful():
    return render_template("unsucc.html")

@app.route("/reg")
def register():
    return render_template("register.html")

@app.route("/emplist")
def emp_list():
    el = selectAllEmp()
    return render_template("emplist.html", elist=el)

@app.route("/update")
def update():
    el = selectAllEmp()
    return render_template("update.html",elist=el)

@app.route("/login")
def login():
    el = selectAllEmp()
    return render_template("login.html",elist=el)

@app.route("/addEmp", methods=["POST"])
def add_emp():
    ide = request.form['id']
    name = request.form['name']
    contact = request.form['contact']
    email = request.form['email']
    passw = request.form['passw']

    t = (ide, name,contact, email, passw)
    addEmp(t)
    return redirect("/")

@app.route("/deleteEmp",methods=["POST"])
def del_emp():
    ide = request.form['id']
    deleteEmp(ide)

    return redirect("/emplist")

@app.route("/updateEmp",methods=["POST"])
def update_emp():
    name = request.form['name']
    contact = request.form['contact']
    email = request.form['email']
    passw = request.form['passw']
    ide = request.form['id']

    t = (name, contact, email, passw, ide)
    updateEmp(t)
    return redirect("/")

@app.route("/checkEmp",methods=["POST"])
def check_emp():
    email = request.form['email']
    passw = request.form['password']
    elist = checkEmp()
    if ((email,passw)in elist):
        return render_template('succ.html')
    else:
        return render_template("unsucc.html")


if(__name__=="__main__"):
    app.run()
