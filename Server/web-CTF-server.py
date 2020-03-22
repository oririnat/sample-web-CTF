from flask import Flask, render_template, request, session, redirect, url_for
import csv

app = Flask(__name__)

@app.route("/register_to_system", methods=["POST"])
def register_to_system():
	form_username = request.form["username"]
	form_password = request.form["pass"]

	users_file = open('data/users.csv', 'a')
	users_file.write(form_username + "," + form_password + ", 0\n")
	users_file.close()

	return redirect(url_for('login'))

@app.route("/try_login_to_page", methods=["post"])
def try_login_to_page():
	session['username'] = request.form["username"]
	session['pass'] = request.form["pass"]
	if(isUserLogin(session['username'], session['pass'])):
		return redirect(url_for('index'))
	else:
		return redirect(url_for('login'))

def isUserLogin(form_username, form_password):
	with open('data/users.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if(row[0] == form_username and row[1] == form_password):
				return True;
	return False

@app.route("/transfer-money")
def transfer_money():
	return "OK"

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/login", methods=["get"])
def login():
	if(isUserLogin(session['username'], session['pass'])):
		return redirect(url_for('index'))
	else:
		return render_template("login.html")

@app.route("/logout")
def logout():
	session.pop('username')
	session.pop('pass')
	return render_template("login.html")

@app.route("/")
def home():
	if(isUserLogin(session['username'], session['pass'])):
		return render_template("index.html")
	else:
		return render_template("login.html")

@app.route("/index")
def index():
	if(isUserLogin(session['username'], session['pass'])):
		return render_template("index.html")
	else:
		return render_template("login.html")

@app.route("/about")
def about():
	if(isUserLogin(session['username'], session['pass'])):
		return render_template("about.html")
	else:
		return render_template("login.html")

@app.route("/blog")
def blog():
	if(isUserLogin(session['username'], session['pass'])):
		return render_template("blog.html")
	else:
		return render_template("login.html")

@app.route("/single-blog")
def single_blog():
	if(isUserLogin(session['username'], session['pass'])):
		return render_template("single-blog.html")
	else:
		return render_template("login.html")

@app.route("/project")
def project():
	if(isUserLogin(session['username'], session['pass'])):
		return render_template("project.html")
	else:
		return render_template("login.html")

@app.route("/project_details")
def project_details():
	if(isUserLogin(session['username'], session['pass'])):
		return render_template("project_details.html")
	else:
		return render_template("login.html")

@app.route("/service")
def service():
	if(isUserLogin(session['username'], session['pass'])):
		return render_template("service.html")
	else:
		return render_template("login.html")

@app.route("/elements")
def elements():
	if(isUserLogin(session['username'], session['pass'])):
		return render_template("elements.html")
	else:
		return render_template("login.html")

@app.route("/contact")
def contact():
	if(isUserLogin(session['username'], session['pass'])):
		return render_template("contact.html")
	else:
		return render_template("login.html")

if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	username = 'admin'
	password = 'admin'
	users = ""

	app.run(debug=True)
