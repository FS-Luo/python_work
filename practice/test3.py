# 定义一个列表，并将列表中的头尾两个元素对调

def swaplist(newlist):
    newlist[0], newlist[-1] = newlist[-1], newlist[0]
    return

list1 = list(range(5))
list2 = list('abcdefg')

print(list1)
print(list2)

swaplist(list1)
swaplist(list2)

print(list1)
print(list2)

