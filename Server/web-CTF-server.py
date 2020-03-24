from flask import Flask, render_template, request, session, redirect, url_for
import csv
from datetime import timedelta, date

app = Flask(__name__)

@app.route("/register_to_system", methods=["POST"])
def register_to_system():
	form_username = request.form["username"]
	form_password = request.form["pass"]
	if(not isUserNameExist(form_username)):
		users_file = open('data/users.csv', 'a')
		currID = file_len('data/users.csv');
		users_file.write(form_username + "," + form_password + "," + str(currID) + "\n")
		users_file.close()
		accounts_file = open('data/accounts.csv', 'a')
		accounts_file.write(str(currID) + ",0," + str(date.today()) + "\n")
		accounts_file.close()
		return redirect(url_for('login'))
	return render_template("register.html", money=getUserUsernameAndMoney(), invalid='Invalid user username')

@app.route("/try_login_to_page", methods=["post"])
def try_login_to_page():
	session['username'] = request.form["username"]
	session['pass'] = request.form["pass"]
	if(isUserLogin()):
		return redirect(url_for('index'))
	else:
		return redirect(url_for('login'))

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

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
			if((row is not None) and (row[0] == username)):
				return True;
	return False

def addMoney(username, amoutToAdd):
	usersFile = csv.reader(open('data/users.csv'))
	usersLines = list(usersFile)
	for i in range(len(usersLines)):
		if(usersLines[i][0] == username):
			accountsLines = read_file('data/accounts.csv')
			acctID = usersLines[i][2]
			for j in range(len(accountsLines)):
				if(accountsLines[j][0] == acctID):
					if ((int(accountsLines[j][1]) + int(amoutToAdd)) < 0):
						return False
					accountsLines[j][1] = int(accountsLines[j][1]) + int(amoutToAdd)
	writer = csv.writer(open('data/accounts.csv', 'w'))
	writer.writerows(accountsLines)
	return True

def read_file(file):
    with open(file, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data

def getUserUsernameAndMoney():
	accountDetails = getAccountDetails()
	if not(accountDetails == 0):
		return session['username'] + " has " + accountDetails[1]

def getAccountDetails():
	if 'username' not in session:
		return 0
	with open('data/users.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if(row[0] == session['username']):
				accountsLines = read_file('data/accounts.csv')
				for i in range(len(accountsLines)):
					if(int(accountsLines[i][0]) == int(row[2])):
						return accountsLines[i]

@app.route("/transfer-money", methods=["post"])
def transfer_money():
	if 'username' not in session:
		return render_template("login.html")

	form_sendTo = request.form["sendTo"]
	form_amount = request.form["amount"]

	if(not isUserNameExist(form_sendTo)):
		return render_template("index.html", money=getUserUsernameAndMoney(), transferMoneyMessage="There is no such user name")

	if(addMoney(session['username'], -1 * int(form_amount))):
		addMoney(form_sendTo, form_amount)
		return render_template("index.html", money=getUserUsernameAndMoney(), transferMoneyMessage="Money transfered successfully")

	else:
		return render_template("index.html", money=getUserUsernameAndMoney(), transferMoneyMessage="You dont have enough money")


@app.route("/register")
def register():
	return render_template("register.html", money=getUserUsernameAndMoney())

@app.route("/login", methods=["get"])
def login():
	if(isUserLogin()):
		return redirect(url_for('/'))
	else:
		return render_template("login.html")

@app.route("/logout")
def logout():
	if 'username' not in session or 'pass' not in session:
		return render_template("login.html")
	session.pop('username')
	session.pop('pass')
	return render_template("login.html")

@app.route("/")
def home():
	if(isUserLogin()):
		return render_template("index.html", money=getUserUsernameAndMoney())
	else:
		return render_template("login.html")

@app.route("/index")
def index():
	if(isUserLogin()):
		return render_template("index.html", money=getUserUsernameAndMoney())
	else:
		return render_template("login.html")

@app.route("/my_account")
def my_account():
	if(isUserLogin()):
		return render_template("my_account.html", money=getUserUsernameAndMoney(), accountDetails=getAccountDetails())
	else:
		return render_template("login.html")

@app.route("/chickenyoualmostthereaccounts")
def accounts():
	if(isUserLogin()):
		import tablib
		import os
		dataset = tablib.Dataset()
		with open(os.path.join(os.path.dirname(__file__),'data/accounts.csv')) as f:
			dataset.csv = f.read()
		return dataset.html
	else:
		return render_template("login.html")


@app.route("/blog")
def blog():
	if(isUserLogin()):
		return render_template("blog.html", money=getUserUsernameAndMoney())
	else:
		return render_template("login.html")

@app.route("/single-blog")
def single_blog():
	if(isUserLogin()):
		return render_template("single-blog.html", money=getUserUsernameAndMoney())
	else:
		return render_template("login.html")

@app.route("/project")
def project():
	if(isUserLogin()):
		return render_template("project.html", money=getUserUsernameAndMoney())
	else:
		return render_template("login.html")

@app.route("/project_details")
def project_details():
	if(isUserLogin()):
		return render_template("project_details.html", money=getUserUsernameAndMoney())
	else:
		return render_template("login.html")

@app.route("/service")
def service():
	if(isUserLogin()):
		return render_template("service.html", money=getUserUsernameAndMoney())
	else:
		return render_template("login.html")

@app.route("/elements")
def elements():
	if(isUserLogin()):
		return render_template("elements.html", money=getUserUsernameAndMoney())
	else:
		return render_template("login.html")

@app.route("/contact")
def contact():
	if(isUserLogin()):
		return render_template("contact.html", money=getUserUsernameAndMoney())
	else:
		return render_template("login.html")

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