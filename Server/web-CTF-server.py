from flask import Flask, render_template, request, session, redirect, url_for,make_response
import csv
from datetime import timedelta, date
import pandas as pd

app = Flask(__name__)

@app.route("/register_to_system", methods=["POST"])
def register_to_system():
	form_username = request.form["username"]
	form_password = request.form["pass"]
	if(not isUserNameExist(form_username)):
		users_file = open('data/users.csv', 'a')
		users_file.write(form_username + "," + form_password + "," + str(nextUserId()) + "\n")
		users_file.close()
		accounts_file = open('data/accounts.csv', 'a')
		accounts_file.write(str(nextUserId() - 1) + ",0," + str(date.today()) + "," + form_username +"\n")
		accounts_file.close()
		return redirect(url_for('login'))
	return render_template("register.html", money=getCurrAccount()[1], username=getCurrUsername(), invalid='Invalid user username')

@app.route("/try_login_to_page", methods=["post"])
def try_login_to_page():
	with open('data/users.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if(row[0] == request.form["username"] and row[1] == request.form["pass"]):
				response = make_response(redirect('/'))
				response.set_cookie('token', value=row[2], max_age=None)
				session['tokenId'] = row[2]
				return response
	return render_template("register.html", money=getCurrAccount()[1], username=getCurrUsername(), invalid='Error')

def isUserLogin():
	if not request.cookies.get('token'):
		return False
	else:
		with open('data/accounts.csv', 'r') as accounts:
			accountsReader = csv.reader(accounts)
			for account in accountsReader:
				if(account[0] == request.cookies.get('token')):
					return True;
	return False

def nextUserId():
	lastRow = None
	with open('data/users.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			lastRow = row
	if(lastRow != None):
		return int(lastRow[2]) + 1
	return 0

def isUserNameExist(username):
	with open('data/users.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if((row is not None) and (row[0] == username)):
				return True;
	return False

@app.route("/transfer-money", methods=["post"])
def transfer_money():
	if not request.cookies.get('token'):
			return render_template("login.html")
	else:
		form_sendTo = request.form["sendTo"]
		form_amount = request.form["amount"]

		if(not isUserNameExist(form_sendTo)):
			return render_template("index.html", money=getCurrAccount()[1], username=getCurrUsername(), transferMoneyMessage="There is no such user name")

		if(addMoney(session['tokenId'], -1 * int(form_amount))): # fix me
			addMoney(getIdFromUsername(form_sendTo), form_amount)
			return render_template("index.html", money=getCurrAccount()[1], username=getCurrUsername(), transferMoneyMessage="Money transfered successfully")

		else:
			return render_template("index.html", money=getCurrAccount()[1], username=getCurrUsername(), transferMoneyMessage="You dont have enough money")

def addMoney(tokenId, amoutToAdd):
	accountsLines = read_file('data/accounts.csv')
	for j in range(len(accountsLines)):
		if(accountsLines[j][0] == tokenId):
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

def getCurrUsername():
	accountDetails = getCurrAccount()
	if (accountDetails == 0):
		return 'error'
	else:
		return accountDetails[3]

def getAccountByID(acct_id):
	accountsLines = read_file('data/accounts.csv')
	for i in range(len(accountsLines)):
		if(accountsLines[i][0] == acct_id):
			return accountsLines[i]
	return 0

def getCurrAccount():
	curr_id = request.cookies.get('token')
	if not curr_id:
		return 0
	else:
		return getAccountByID(curr_id)

def getIdFromUsername(username):
	with open('data/users.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if(row[0] == username):
				return row[2]
				
def isUserIsAdmin():
	accountsLines = read_file('data/accounts.csv')
	for i in range(len(accountsLines)):
		if(accountsLines[i][0] == request.cookies.get('token') and accountsLines[i][3] == 'admin'):
			return True
	return False

@app.route("/register")
def register():
	return render_template("register.html", money=getCurrAccount()[1], username=getCurrUsername())

@app.route("/login", methods=["get"])
def login():
	return render_template("login.html")

@app.route("/logout")
def logout():
	if not request.cookies.get('token'):
		return render_template("login.html")
	resp = make_response(render_template("login.html"))
	resp.set_cookie('token', expires=0)
	session['tokenId'] = ''
	return resp

@app.route("/")
def home():
	if(isUserLogin()):
			return render_template("index.html", money=getCurrAccount()[1], username=getCurrUsername())
	else:
		return render_template("login.html")

@app.route("/index")
def index():
	if(isUserLogin()):
		if(isUserIsAdmin()):
			return render_template("index.html", money=getCurrAccount()[1], username=getCurrUsername(), adminBotton="<p>text</p>")
		return render_template("index.html",money=getCurrAccount()[1], username=getCurrUsername())
	else:
		return render_template("login.html")

@app.route("/my_account")
def my_account():
	if(isUserLogin()):
		return render_template("my_account.html", money=getCurrAccount()[1], username=getCurrUsername(), accountDetails=getCurrAccount())
	else:
		return render_template("login.html")

@app.route("/chickenyoualmostthereaccounts")
def accounts():
	if(isUserLogin()):
		columns = ['Account ID', 'Money', 'Joining Date']
		df = pd.read_csv("data/accounts.csv", names=columns)
		return render_template("accounts.html", money=getCurrAccount()[1], username=getCurrUsername(), accountDetails=getCurrAccount(), accounts=df.to_html())
	else:
		return render_template("login.html")

@app.route("/blog")
def blog():
	if(isUserLogin()):
		return render_template("blog.html", money=getCurrAccount()[1], username=getCurrUsername())
	else:
		return render_template("login.html")

@app.route("/single-blog")
def single_blog():
	if(isUserLogin()):
		return render_template("single-blog.html", money=getCurrAccount()[1], username=getCurrUsername())
	else:
		return render_template("login.html")

@app.route("/project")
def project():
	if(isUserLogin()):
		return render_template("project.html", money=getCurrAccount()[1], username=getCurrUsername())
	else:
		return render_template("login.html")

@app.route("/project_details")
def project_details():
	if(isUserLogin()):
		return render_template("project_details.html", money=getCurrAccount()[1], username=getCurrUsername())
	else:
		return render_template("login.html")

@app.route("/service")
def service():
	if(isUserLogin()):
		return render_template("service.html", money=getCurrAccount()[1], username=getCurrUsername())
	else:
		return render_template("login.html")

@app.route("/elements")
def elements():
	if(isUserLogin()):
		return render_template("elements.html", money=getCurrAccount()[1], username=getCurrUsername())
	else:
		return render_template("login.html")

@app.route("/contact")
def contact():
	if(isUserLogin()):
		return render_template("contact.html", money=getCurrAccount()[1], username=getCurrUsername())
	else:
		return render_template("login.html")

if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'

	app.run(debug=True)