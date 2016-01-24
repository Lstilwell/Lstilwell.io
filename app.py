from flask import Flask, jsonify, render_template,request

import requests


#Flask 'app' variable that we use to access info about the server
app = Flask(__name__)


#---When user clicks button- POST request will send us here---

#Default: GET- go to the webpage, use POST if user submits form
@app.route("/search", methods=["GET","POST"])
def search():

	if request.method =="POST":
		url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
		response_dict = requests.get(url).json()
		return jsonify(response_dict)
	else:
		return render_template("search.html")

	# return render_template("websiteBody.html")




#Server will start accepting requests from the client
if __name__ == "__main__":
	#Hosted locally
	app.run(host = "0.0.0.0")


