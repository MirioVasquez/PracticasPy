from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/frm')
def pdg():
    return render_template('formulario.html')

@app.route('/exc')
def exc():
    return render_template('exc.html')

@app.route('/brdr')
def brdr():
    return render_template('brdr.html')

@app.route('/grdt')
def grdt():
    return render_template('grdt.html')

@app.route('/terminos')
def terminos():
    return render_template('terminos.html')

if __name__ == '__main__':
    app.run(debug=True)