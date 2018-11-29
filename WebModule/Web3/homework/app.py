from flask import Flask, render_template, request
import mlab
from bike import Bike

mlab.connect()
app = Flask(__name__)

@app.route("/new_bike", methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("new_bike.html")
    elif request.method == "POST":
        form = request.form
        model = form['model']
        dailyfee = form['dailyfee']
        img = form['image']
        year = form['year']
        b = Bike(model = model, dailyfee = dailyfee, image = img, year = year)
        # print(b)
        b.save()
        return "success"

if __name__ == "__main__":
    app.run(debug = True)