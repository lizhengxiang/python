from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Hello World!<h2>'

@app.route('/user/<name>')
def user(name):
	return '<h1>hello, %s</h1>' % name
if __name__ == '__main__':
    app.run(debug=True)
	#app.run(host='0.0.0.0')
