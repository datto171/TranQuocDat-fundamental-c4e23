from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<name>")
def posts(name):
    Users  = {
        'huy'     : {
                        'name': 'Nguyen Quang Huy',
                        'age': 29
                    },
        'tuan anh': {
                        'name': 'Huynh Tuan Anh',
                        'age': 22
                    }
    }
    if name in Users:
        return render_template("user.html", name = Users[name]['name'], age = Users[name]['age'])
    else:
        return "User not found"
if __name__ == "__main__":
    app.run()