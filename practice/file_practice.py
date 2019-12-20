with open('file_practice.txt', 'w') as f:
	num = f.write('\t人生苦短，我用Python!\n\
	不仅要学习Python，还要学习web前端开发!\n\
	需要学习HTML, CSS, JaveScript!\n')
	print(num)

with open('file_practice.txt', 'r') as f:
	# 方法read()
	content = f.read()
	print(content, end='')

	# 遍历文件
	for row in f:
		print(row, end='')
	
	# 方法readline()
	while True:
		row = f.readline()
		print(row, end='')
		if row == '':
			break		
	
	# 方法readlines()
	rows = f.readlines()
	for row in rows:
		print(row, end='')
	

# ~ with open('practice.txt', 'r') as f:
	# ~ content = f.read()
	# ~ print(content, end='')
	
	# ~ for row in f:
		# ~ print(row, end='')
	
	# ~ while True:
		# ~ row = f.readline()
		# ~ print(row, end='')
		# ~ if row == '':
			# ~ break		
	
	# ~ rows = f.readlines()
	# ~ for row in rows:
		# ~ print(row, end='')
	
	
	
