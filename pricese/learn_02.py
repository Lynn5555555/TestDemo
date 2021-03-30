#分支结构 if:  else:
a = 1
if a == 0:
    print("a=0")
elif a == 1:
    print("a==1")
else:
    print("a!=0 && a!=1")


#循环接口 for-in  while
'''计算1-100的和'''
result = 0
for i in range(101):
    print(i)
    result = result + i
print(result)

a = 1
while a == 1:
    print("a==1")
    a = a+1
else:
    print("a!=1")
    print(a)
