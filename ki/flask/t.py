from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    return render_template("home.html")

@app.route("/admin/",methods=["GET","POST"])
def admin():   
     if (request.method == "POST"):
          admi={"kishore":"krish","methil":"power"}
          k=request.form["username"]
          if k in admi:
               return redirect("/loggidin/")
          else:
               return redirect("/invalid/")
     
     return render_template("admin.html")
@app.route("/loggidin/",methods=["POST","GET"])
def loggid():
     return render_template("loggidin.html")

@app.route("/invalid/",methods=["POST","GET"])
def inva():
     return render_template("invalid.html")

@app.route("/user/",methods=["GET","POST"])
def user():
     if (request.method == "POST"):
          users={"kishore":"krishna","methil":"pubg"}
          t=request.form["username"]
          if t in users:
               return redirect("/correct/")
          else:
               return redirect("/invalid/")
     
     return render_template("user.html")

@app.route("/correct/",methods=["POST","GET"])
def logg():
     return render_template("correct.html")

@app.route("/invalid/",methods=["POST","GET"])
def inv():
     return render_template("invalid.html")
    



