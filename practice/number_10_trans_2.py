def mybin(n_10):
	"""自定义十进制转二进制"""
	n_2 = bin(n_10).replace('0b', '')
	return n_2

def myoct(n_10):
	"""自定义十进制转八进制"""
	n_8 = oct(n_10).replace('0o', '')
	return n_8

def myhex(n_10):
	"""自定义十进制转十六进制"""
	n_16 = hex(n_10).replace('0x', '')
	return n_16


