from flask import Flask, render_template, jsonify, request, session, redirect, url_for, make_response
import csv
import datetime
from datetime import date
import jwt
import hashlib
from functools import wraps

app = Flask(__name__)

def token_requird(f):
	@wraps(f)
	def decorated(*args, **Kwargs):
		token = request.cookies.get('token')
		if not token:
			return render_template("login.html")
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return render_template("login.html")
		return f(*args, **Kwargs)
	return decorated

def moveToPageAndUpdateToken(path):
	token = request.cookies.get('token')
	if not token:
		return render_template("login.html")
	try:
		data = jwt.decode(token, app.config['SECRET_KEY'])
		token = jwt.encode({'user' : data['user'], 'id' : data['id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds = 60 * 60 * 2)}, app.config['SECRET_KEY'])
		response = make_response(render_template(path, money=getUserData()[1], username=getUserData()[3]))
		response.set_cookie('token', value=token.decode('UTF-8'), max_age=None)
		return response
	except:
		return render_template("login.html")

@app.route("/register_to_system", methods=["POST"])
def register_to_system():
	form_username = request.form["username"]
	form_password = request.form["pass"]
	if(not isUserNameExist(form_username)):
		users_file = open('data/users.csv', 'a')
		users_file.write(form_username + "," + getSecurePassword(form_password) + "," + str(nextUserId()) + "\n")
		users_file.close()
		accounts_file = open('data/accounts.csv', 'a')
		accounts_file.write(str(nextUserId() - 1) + ",0," + str(date.today()) + "," + form_username +"\n")
		accounts_file.close()
		return redirect(url_for('login'))
	return render_template("register.html", invalid='Invalid user username')

@app.route("/try_login_to_page", methods=["post"])
def try_login_to_page():
	currUserName = request.form["username"]
	currPassword = getSecurePassword(request.form["pass"])
	with open('data/users.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if(row[0] == currUserName and row[1] == currPassword):
				token = jwt.encode({'user' : request.form["username"],
									'id' : row[2],
				 					'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds = 60 * 60 * 2)},
									 app.config['SECRET_KEY'])
				response = make_response(redirect('/'))
				response.set_cookie('token', value=token.decode('UTF-8'), max_age=None)
				return response
	return render_template("register.html", invalid='Error')

def getSecurePassword(plainPassword):
	return hashlib.sha256(plainPassword + app.config['SALT_FOR_HASH']).hexdigest()

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
			return render_template("index.html", money=getUserData()[1], username=getUserData()[3], transferMoneyMessage="There is no such user name")

		if(addMoney(getDataFromJWT()['id'], -1 * int(form_amount))): # fix me
			addMoney(getIdFromUsername(form_sendTo), form_amount)
			return render_template("index.html", money=getUserData()[1], username=getUserData()[3], transferMoneyMessage="Money transfered successfully")
		else:
			return render_template("index.html", money=getUserData()[1], username=getUserData()[3], transferMoneyMessage="You dont have enough money")

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

def getDataFromJWT():
	token = request.cookies.get('token')
	if not token:
		return render_template("login.html")
	try:
		return jwt.decode(token, app.config['SECRET_KEY'])
	except:
		return render_template("login.html")

def getUserData():
	userId = getDataFromJWT()['id']
	accountsLines = read_file('data/accounts.csv')
	for i in range(len(accountsLines)):
		if(accountsLines[i][0] == userId):
			return accountsLines[i]
	return 'error'

def getIdFromUsername(username):
	with open('data/users.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			if(row[0] == username):
				return row[2]

def isUserIsAdmin():
	accountsLines = read_file('data/accounts.csv')
	for i in range(len(accountsLines)):
		if(accountsLines[i][0] == getDataFromJWT()['id'] and accountsLines[i][3] == 'admin'):
			return True
	return False

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/login", methods=["get"])
def login():
	return render_template("login.html")

@app.route("/logout")
def logout():
	if not request.cookies.get('token'):
		return render_template("login.html")
	resp = make_response(render_template("login.html"))
	resp.set_cookie('token', expires=0)
	return resp

@app.route("/")
@token_requird
def home():
	return moveToPageAndUpdateToken("index.html")

@app.route("/index")
@token_requird
def index():
	return moveToPageAndUpdateToken("index.html")

@app.route("/my_account")
@token_requird
def my_account():
	return render_template("my_account.html", money=getUserData()[1], username=getUserData()[3], accountDetails=getUserData())

@app.route("/chickenyoualmostthereaccounts")
@token_requird
def accounts():
	if isUserIsAdmin():
		messages = []
		messages.append("<table>")
		messages.append("<th>")
		messages.append("<td>Account ID</td>")
		messages.append("<td>Money</td>")
		messages.append("<td>Joining Date</td>")
		messages.append("</th>")

		with open('data/accounts.csv', 'r') as file:
			reader = csv.reader(file)
			accountsList = list(reader)

		return render_template("accounts.html", money=getUserData()[1], username=getUserData()[3], accountDetails=getUserData(), len=len(accountsList), accounts=accountsList)
	return render_template("not_authorized.html", money=getUserData()[1], username=getUserData()[3])

@app.route("/blog")
@token_requird
def blog():
	return moveToPageAndUpdateToken("blog.html")

@app.route("/single-blog")
@token_requird
def single_blog():
	return moveToPageAndUpdateToken("single-blog.html")

@app.route("/project")
@token_requird
def project():
	return moveToPageAndUpdateToken("project.html")

@app.route("/project_details")
@token_requird
def project_details():
	return moveToPageAndUpdateToken("project_details.html")

@app.route("/service")
@token_requird
def service():
	return moveToPageAndUpdateToken("service.html")

@app.route("/elements")
@token_requird
def elements():
	return moveToPageAndUpdateToken("elements.html")

@app.route("/contact")
@token_requird
def contact():
	return moveToPageAndUpdateToken("contact.html")

if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.config['SECRET_KEY'] = 'jwtSecretKey!@#'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.config['SALT_FOR_HASH'] = 'thisIsSecretSalt'

	app.run(debug=True)
