# 算法一： 每次都调用已计算出的质数列表，来简化后续质数检验
zhishu_1 = [2]
for n in range(2, 1000000):
	for k in zhishu_1:
		if n % k == 0:
			break
	else:
		zhishu_1.append(n)

# 算法二： 每次都从2开始整除检验，直到除尽或遍历结束。效率较低
zhishu_2 = []
# ~ for n in range(2, 100000):
	# ~ for k in range(2, n):
		# ~ if n % k == 0:
			# ~ break
	# ~ else:
		# ~ zhishu_2.append(n)

print(len(zhishu_1),len(zhishu_2))
