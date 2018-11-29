from flask import Flask, render_template, request
import mlab
from movie import Movie
from register import Register

mlab.connect()
app = Flask(__name__)

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "GET":
        #User request form
        return render_template("add_movie.html")
    elif request.method == "POST":
        form = request.form
        t = form['title']
        img = form['image']
        y = form['year']
        m = Movie(title = t, image = img, year = y)
        m.save()
        return "GotCha!!!"
    
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        u = form['user']
        p = form['pass']
        e = form['email']

        exist_user = Register.objects(username = u).first()
        if exist_user != None:
            return "User has been already exist !" 
        else:
            r = Register(username = u, password = p, email = e)
            r.save()
            return "GotCha!!!"

if __name__ == "__main__":
    app.run(debug = True)