from flask import Flask, render_template , request
app = Flask(__name__)

@app.route('/')
def playground():
    return render_template('playground.html',num =int(1))

@app.route('/play')
def play():
    return render_template("play.html", num = int(3))

@app.route('/play/<num>')
def playx(num):
    return render_template('play.html', num = int(num))

@app.route('/play/<num>/<color>')
def colors(num, color):
    return render_template('play.html', num = int(num), box_color = color)

# @app.route('/process', methods=['POST'])
# def process_form():
#     print('*********************************************')
#     print(request.form)

if __name__=="__main__":
    app.run(debug=True)