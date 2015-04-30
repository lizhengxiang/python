phonebook = {'lzx' : '123', 'lzq' : '456'}
print "lizhengxiang phone number %(lzx)s"% phonebook
#print a

template = '''<html>
	<head><title>%(title)s</title></head>
	<body>
	<h1>%(title)s</h>
	<p>%(text)s</p>
	</body>'''
data = {'title' : 'my love page', 'text' : 'welcome to my home page!'}
print template % data
#<html>
#<head><title>my home page</title></head>
#<body>
#<h1>my home page</h1>
#<p> welcome to my home page!</p>
#</body>

x = {'username':['admi', 'ber']}
y = x.copy()
y['username'] = 'mlh' 
print y
y['username'].remove('ber')
print x
