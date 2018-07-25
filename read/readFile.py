from flask import Flask
import os.path
app=Flask("d")
@app.route("/")
def index():
	if os.path.isfile("/data/abc.txt")==False:
		return "sorry"
	with open("/data/abc.txt","r") as f:
		data=f.read()
	return data
	
app.run(host="0.0.0.0",port=3000,debug=True)
