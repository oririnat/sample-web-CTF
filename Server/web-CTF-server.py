from flask import Flask, render_template, request, session, redirect, url_for
import csv
from datetime import timedelta

app = Flask(__name__)

@app.route("/register_to_system", methods=["POST"])
def register_to_system():
	form_username = request.form["username"]
	form_password = request.form["pass"]
	if(not isUserNameExist(form_username)):
		users_file = open('data/users.csv', 'a')
		users_file.write(form_username + "," + form_password + ", 0\n")
		users_file.close()
		return redirect(url_for('login'))
	return render_template("register.html", money=getUserMoney(), invalid='Invalid user username')

@app.route("/try_login_to_page", methods=["post"])
def try_login_to_page():
	session['username'] = request.form["username"]
	session['pass'] = request.form["pass"]
	if(isUserLogin()):
		return redirect(url_for('index'))
	else:
		return redirect(url_for('login'))

def isUserLogin():
	if 'username' not in session or 'pass' not in session:
		return False
	with open('data/users.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if(row[0] == session['username'] and row[1] == session['pass']):
				return True;
	return False

def isUserNameExist(username):
	with open('data/users.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if(row[0] == username):
				return True;
	return False

def addMoney(username, amoutToAdd):
	usersFile = csv.reader(open('data/users.csv'))
	usersLines = list(usersFile)
	for i in range(len(usersLines)):
		if(usersLines[i][0] == username):
			usersLines[i][2] = int(usersLines[i][2]) + int(amoutToAdd)
	writer = csv.writer(open('data/users.csv', 'w'))
	writer.writerows(usersLines)

def getUserMoney():
	if 'username' not in session:
		return 0
	usersFile = csv.reader(open('data/users.csv'))
	usersLines = list(usersFile)
	for i in range(len(usersLines)):
		return usersLines[i][2]

@app.route("/transfer-money")
def transfer_money():
	return "OK"

@app.route("/register")
def register():
	return render_template("register.html", money=getUserMoney())

@app.route("/login", methods=["get"])
def login():
	if(isUserLogin()):
		return redirect(url_for('/'))
	else:
		return render_template("login.html", money=getUserMoney())

@app.route("/logout")
def logout():
	if 'username' not in session or 'pass' not in session:
		return render_template("login.html", money=getUserMoney())
	session.pop('username')
	session.pop('pass')
	return render_template("login.html", money=getUserMoney())

@app.route("/")
def home():
	if(isUserLogin()):
		return render_template("index.html", money=getUserMoney())
	else:
		return render_template("login.html", money=getUserMoney())

@app.route("/index")
def index():
	if(isUserLogin()):
		return render_template("index.html", money=getUserMoney())
	else:
		return render_template("login.html", money=getUserMoney())

@app.route("/blog")
def blog():
	if(isUserLogin()):
		return render_template("blog.html", money=getUserMoney())
	else:
		return render_template("login.html", money=getUserMoney())

@app.route("/single-blog")
def single_blog():
	if(isUserLogin()):
		return render_template("single-blog.html", money=getUserMoney())
	else:
		return render_template("login.html", money=getUserMoney())

@app.route("/project")
def project():
	if(isUserLogin()):
		return render_template("project.html", money=getUserMoney())
	else:
		return render_template("login.html", money=getUserMoney())

@app.route("/project_details")
def project_details():
	if(isUserLogin()):
		return render_template("project_details.html", money=getUserMoney())
	else:
		return render_template("login.html", money=getUserMoney())

@app.route("/service")
def service():
	if(isUserLogin()):
		return render_template("service.html", money=getUserMoney())
	else:
		return render_template("login.html", money=getUserMoney())

@app.route("/elements")
def elements():
	if(isUserLogin()):
		return render_template("elements.html", money=getUserMoney())
	else:
		return render_template("login.html", money=getUserMoney())

@app.route("/contact")
def contact():
	if(isUserLogin()):
		return render_template("contact.html", money=getUserMoney())
	else:
		return render_template("login.html", money=getUserMoney())

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=2)

if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	username = 'admin'
	password = 'admin'
	users = ""

	app.run(debug=True)
