import pickle

with open('pickle1.pkl', 'rb') as p:
	data1 = pickle.load(p)
	print(data1)
	
	data2 = pickle.load(p)
	print(data2)
