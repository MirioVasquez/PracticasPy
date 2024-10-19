from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! this is the main page <h1>Hello<h1>"

@app.route('/<name>')
def user(name):
    return f"<h1>Hello {name}<h1>"

@app.route('/admin')
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()