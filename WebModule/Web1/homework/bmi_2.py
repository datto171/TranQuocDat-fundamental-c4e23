from flask import Flask, render_template

app = Flask(__name__)

@app.route("/bmi/<int:m>/<int:h>")
def bmi(m, h):
    h = h/100
    bmi = m/h/h 
    if bmi < 16:
        result = "Severely underweight."
    elif bmi < 18.5:
        result = "Underweight."
    elif bmi < 25:
        result = "Normal."
    elif bmi < 30:
        result = "Overweight."
    else:
        result = "Obese."
        
    return render_template("bmi.html", bmi = "%.2f" % bmi, result = result )
if __name__ == "__main__":
    app.run()