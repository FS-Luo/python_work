import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
data2 = [1, 2, 3]

with open('pickle1.pkl', 'wb') as p:
	pickle.dump(data1, p)
	pickle.dump(data2, p)

