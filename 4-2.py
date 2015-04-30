people = {
	'Alice' : {
		'phone' : '2341',
		'addr' : 'Foo drive 23'
	},
	'Beth' : {
		'phone' : '2340',
        'addr' : 'Foo drive 24'
	}
}

labels = {
	'phone' : 'phone number',
	'addr' : 'address'
}

name = raw_input('Name: ')
request = raw_input('phone(p) or address(a)?')
if request == 'p':
	key = 'phone'
if request == 'a':
	key = 'addr' 
person = people.get(name,{})
label = labels.get(key, key)
result = person.get(key, 'not available')
#if name in people:
print"%s's %s is %s." %(name, label, result) 
