database = [
	['lizhangxiang', '1234'],
	['lzx', '12345'],
	['lzq', '1231'],
]

username = raw_input('username: ')
password = raw_input('password: ')
if[username, password] in database:
	print 'Access granted'
else:
	print 'Not Access grantted'
