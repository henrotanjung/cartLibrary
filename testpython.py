a = {}
a['test'] = 5
print (id(a))

total = a
print (id(total))

total['test'] = 3
print (a)
print (total)