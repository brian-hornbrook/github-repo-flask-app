from flask import Flask, render_template
import requests

app = Flask("app")

@app.route('/', methods=["GET"])
def github():
	response = requests.get("https://api.github.com/users/brian-hornbrook")
	response_data = response.json()
	# github_user = response_data["login"]
	return render_template("index.html", data = response_data)

app.run(host='0.0.0.0', port=8000)