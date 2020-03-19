from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/register_to_system", methods=["POST"])
def register_to_system():
	form_username = request.form["username"]
	form_password = request.form["pass"]

	users_file = open('data/users.csv', 'a')
	users_file.write(form_username + "," + form_password + ", 0\n")
	users_file.close()

	return redirect(url_for('login'))

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/login", methods=["get"])
def login():
	# session['username'] = request.args.get('username')
	# session['password'] = request.args.get('password')clear

	return render_template("login.html")



# @app.route("/try_loging", methods=('get', 'post'))
# def try_to_login():
# 	# if(){
# 	#
# 	# }
# 	return True


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


@app.route("/transfer-money")
def transfer_money():

	return "OK"


if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	username = 'admin'
	password = 'admin'
	users = ""

	app.run(debug=True)
