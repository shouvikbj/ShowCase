import os
import smtplib
from flask import Flask,flash,render_template,redirect,request,url_for
import csv

app = Flask(__name__)
app.secret_key = 'Shouvik_Bajpayee'

#Comments
commentstore=["Soumen >> New commenting section is added.. So try it out.. And give some feedback also..","AG >> It's great to see a varied range of clicks equivalent to that of  a professional photographer in a web medium. I congratulate soumen da and shouvik to potray their creative passion in limelight.","Soumen >> Thanks AG. Keep supporting.","ArnabVasudev007 >> Very nice"]

#if not os.getenv("PASSWORD"):
#    raise RuntimeError("Missing Password")

listed = []
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/comments")
def comments():
    return render_template("comments.html", commentstore=commentstore)

@app.route("/Send Comment",methods = ["POST"])
def SendComment():
    usr = request.form.get("username")
    cmnts = request.form.get("comment")
    commentstore.append("{user} >> {cmnt}".format(user=usr,cmnt=cmnts))
    file = open("comments.csv","a")
    writer = csv.writer(file)
    writer.writerow((usr,cmnts))
    file.close()
    return redirect("/comments")


@app.route("/Send Message",methods = ["POST"])
def message():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")
    if not fname or not lname or not email or not subject or not message:
        flash('Please Fill All Fields')
    file = open("messages.csv","a")
    writer = csv.writer(file)
    writer.writerow((fname,lname,email,subject,message))
    file.close()
    message1 = "Welcome to ShowCase..!! We are really looking forward to your suggestions and views. Enjoy your visit to ShowCase."
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login('soumenbajpayee.showcase@gmail.com', 'maathakur60@')
    server.sendmail('soumenbajpayee.showcase@gmail.com', email, message1)
    server.close()
    return redirect(url_for('contact'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
