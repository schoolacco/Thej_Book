from flask import *
import random as rng
app = Flask(__name__)
@app.route('/')
def Hello():
    return "Hello"
@app.route('/test_one')
def Test():
    return str(rng.randint(0,9999999999999999999999999999999999999999999))
@app.route('/custom/<name>')
def Name(name):
    if name == "test":
        return redirect(url_for("Test"))
    else:
        return 'Hello %s!' % name
@app.route('/html')
def html():
    return render_template('test.html')
@app.route('/js')
def js():
    return render_template('test.js')
if __name__ == "__main__":
    app.run(debug= True)