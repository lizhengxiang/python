name = ['lzx', 'lzq', 'lzf', 'llx', 'lyy']
number = ['123', '456','789', '1470', '7854']
print number[name.index('lyy')]

phonbook = {'lzx' : '123', 'lzq' : '456'}

items = [('name','gumby'), ('age', 42)]
d = dict(items)
print d
print len(d)
del d['age']
#d['age'] = 'v'
#print d['age']
print d
d[45] = 'lzx'
print d
print 'name' in d
