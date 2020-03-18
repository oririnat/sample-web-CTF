from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route("/")
def home():
    return session['username']

@app.route("/login", methods=('get', 'post'))
def login():
    session['username'] = request.args.get('username')
    # firstName = request.args.get('first_name')
    return session['username']


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/single-blog")
def single_blog():
    return render_template("single-blog.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/project_details")
def project_details():
    return render_template("project_details.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/elements")
def elements():
    return render_template("elements.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
