from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)
pos=""
@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		pos = request.form["pos"]
		if pos == "consumer":
			return redirect("/signupcons")
		elif pos == "supplier":
			return redirect("/signupsupp")
		elif pos == "vendor":
			return redirect("/signupvend")
		else:
			return render_template("index.html")
	else:
		return render_template("index.html")

@app.route("/signupcons", methods=['GET', 'POST'])
def signupcons():
	if request.method == 'POST':
		email = request.form['email']
		pincode = request.form['pincode']
		mobile_number = request.form['number']
		name = request.form['name']
		username = request.form['txt']
		password = request.form['pswd']
		role = "consumer"  
		data=email+" "+pincode+" "+mobile_number+" "+name+" "+username+" "+password+" "+role
		with open("dat.txt","a") as fh:
			fh.write(data+"\n")
			return render_template("consumer.html")
	else:
		return render_template("consumer.html")
@app.route("/signupvend", methods=['GET', 'POST'])
def signupvend():
	if request.method == 'POST':
		email = request.form['email']
		lisc=request.form['lice']
		pincode = request.form['pincode']
		mobile_number = request.form['number']
		name = request.form['txt']
		username = request.form['username']
		password = request.form['pswd']
		role = "vendor"  
		data=email+" "+pincode+" "+mobile_number+" "+name+" "+username+" "+password+" "+role+" "+lisc
		with open("dat.txt","a") as fh:
			fh.write(data+"\n")
			return render_template("vendor.html")
	else:
		return render_template("vendor.html")
@app.route("/signupsupp", methods=['GET', 'POST'])
def signupsupp():
	if request.method == 'POST':
		email = request.form['email']
		lisc=request.form['lice']
		pincode = request.form['pincode']
		mobile_number = request.form['number']
		name = request.form['txt']
		username = request.form['username']
		password = request.form['pswd']
		role = "supplier"  
		data=email+" "+pincode+" "+mobile_number+" "+name+" "+username+" "+password+" "+role+" "+lisc
		with open("dat.txt","a") as fh:
			fh.write(data+"\n")
			return render_template("supplier.html")
	else:
		return render_template("supplier.html")

counter=False
@app.route("/login",methods=['GET','POST'])
def login():
	global counter,pos
	username=request.form['username']
	password=request.form['pwd']
	with open("dat.txt","r+") as fh:
		lst=fh.readlines()
		for i in lst:
			if username in i:
				print(i.split())
				if i.split()[5]==password:
					pos=i.split()[6]
					counter=True
	if counter==True:
		return redirect(url_for('final',pos=pos))
	else:
		return redirect('/signupcons')

@app.route("/final",methods=['GET','POST'])
def final():
	global pos
	return render_template("final.html",pos=pos)