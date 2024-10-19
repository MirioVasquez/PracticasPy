from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    #return render_template('index.html')
    #return render_template('index1.html', content=name, r=len(name))
    #return render_template('index2.html')
    return render_template('index3.html', content = ['Jorge', 'Carlos', 'Alberto'])
if __name__ == "__main__":
    app.run()