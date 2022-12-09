from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__, static_folder='static/', static_url_path='')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/calander")
def calander():
    return render_template("calander.html")

@app.route("/chats")
def chats():
    return render_template("chats.html")

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)