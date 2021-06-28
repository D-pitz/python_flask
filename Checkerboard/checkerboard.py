from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('checkerboard.html', x=int(8), y=int(8))

@app.route('/<x>')
def checker(x):
    return render_template('checkerboard.html', x=int(x), y=int(8))

@app.route('/<x>/<y>')
def XandY(x,y):
    return render_template('checkerboard.html', x=int(x), y=int(y))

@app.route('/<x>/<y>/<box1>/<box2>')
def custom(x,y,box1,box2):
    return render_template('checkerboard.html', x=int(x), y=int(y), box1=box1, box2=box2)

if __name__=="__main__":
    app.run(debug=True)