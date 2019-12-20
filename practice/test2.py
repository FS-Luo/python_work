# 计算n个自然数的立方和

def sumcubes(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    print(sum)

try:
    n = int(input('Enter a int number:'))
except ValueError:
    print('It must be a int number!')
else:
    sumcubes(n)

