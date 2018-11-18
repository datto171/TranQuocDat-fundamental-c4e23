from flask import Flask, render_template

app = Flask(__name__)

#function binding -  neu nguoi dung vao trang chu thi goi vao ham nay cho tao
@app.route("/")
def home():
    return "Hello Flask"

@app.route("/c4e")
def c4e():
    return "Hello c4e 12312"

@app.route("/me")
def me():
    return "Alo 1234 Nam sau bay"

@app.route("/hi/<name>")
def hi_name(name):
    return "Hello " + name

@app.route("/add/<int:x>/<int:y>")
def add(x, y):
    s = x + y
    return str(s)

@app.route("/posts/<int:index>")
def posts(index):
    titles = [
        "Trời mưa to quá", 
        "Trời nắng",
        "Trời"
    ]
    content = [
        "Buồn ngủ quá ",
        "Đen",
        "Ngủ"
    ]
    c = content[index]
    t = titles[index]
    return render_template("post.html", title = t, content = c)

@app.route("/movie")
def movie():
    return render_template("movie.html", name='batman', img='https://media.comicbook.com/2018/06/batman-ben-affleck-rumor-matt-reeves-movie-1113820-1280x0.jpeg')

@app.route("/movies")
def movies():
    list_movies = [
        {
            'title': 'dead',
            'image': 'https://media.comicbook.com/2018/06/batman-ben-affleck-rumor-matt-reeves-movie-1113820-1280x0.jpeg'
        },
        {
            'title': 'bat man',
            'image': 'https://www.w3schools.com/w3css/img_lights.jpg'
        },
        {
            'title': 'x-men',
            'image': 'https://cdn.pixabay.com/photo/2013/04/06/11/50/image-editing-101040_960_720.jpg'
        }
    ]

    return render_template("movies.html", movies = list_movies)

if __name__ == "__main__":
    app.run(debug = True)