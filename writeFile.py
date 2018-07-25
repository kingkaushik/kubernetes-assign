from flask import Flask,render_template,request
import os.path
app=Flask("first")
@app.route("/")
def index():
	return render_template("ind.html")




@app.route("/abc",methods=['POST'])
def new():
	data=request.form['data']
	with open("/data/abc.txt","a") as f:
		f.write("{}<br>".format(data))
	return data+" written into text file"
	
app.run(host="0.0.0.0",debug=True,port=4000)
