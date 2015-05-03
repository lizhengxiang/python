#from flask import Flask
#from flask.ext.script import Manager
#from flask import redirect
#from flask import request
#from flask import make_response
#from flask import abort
#app = Flask(__name__)
#manager = Manager(app)
#@app.route('/')
#def index():
#   return '<h2>Hello World!<h2>' , 400
#    return redirect('http://www.baidu.com')

#@app.route('/user/<name>')
#def index():
	#return '<h1>hello, %s</h1>'
#	user_agent = request.headers.get('User-Agent')
#	return '<p> your bowser is %s</p>' % user_agent

#@app.route('/')	
#def index():
#	response = make_response('<h1>hello lilzhengxiag</h1>')
#	response.set_cookie('answer', '42')
#	return response
#@app.route('/user/<id>')
#def get_uesr(id):
#	user = load_user(id)
#	if not user:
#		abort(404)
#	return '<h1>hello %s </h1>' %user.name
		
#if __name__ == '__main__':
#    manager.run(debug=True)
#app.run(host='0.0.0.0')
