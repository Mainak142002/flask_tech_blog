from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

blogs = [
    {"title": "Python", "author": "mainak dey", "desc": "Good for programming..."},
    {"title": "Hi Tech", "author": "mainak dey", "desc": "AI is future..."}
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/blogs')
def show_blogs():
    return render_template("blogs.html", blogs=blogs)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print(request.form)
        return redirect(url_for('home'))
    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.form)
        return redirect(url_for('home'))
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
