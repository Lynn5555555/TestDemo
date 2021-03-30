# list 列表
list_a = [2, 3, 4, 5, 7, 6]
list_a.append(0)
list_a.insert(0, 1)
list_a.remove(1)
list_a.pop(2)
list_a.sort()
list_a.sort(reverse=True)
print(list_a)

# 平方列表
list_b = [i ** 2 for i in range(1, 4)]
print(list_b)

list_C = []
for i in range(1, 4):
    if i != 1:
        list_C.append(i ** 2)
print(list_C)

list_d = [i ** 2 for i in range(1, 4) if i != 1]
print(list_d)

list_e = []
for i in range(1, 4):
    for j in range(1, 4):
        list_e.append(i * j)
print(list_e)

list_f = [i * j for i in range(1, 4) for j in range(1, 4)]
print(list_f)
print(type(list_f))

# 元祖
tuple_a = (1, 2, 3)
tuple_b = 1, 2, 3
print(tuple_a)
print(type(tuple_a))
print(tuple_b)
print(type(tuple_b))

# 元祖的不可变特性
list_g = [1, 2, 3]
list_g[0] = 'a'
print(list_g)

# tuple_c = (1, 2, 3)
# tuple_c[0] = 'a'
# print(tuple_c)

# 元祖可以嵌套列表
tuple_d = (1, 2, list_g)
print(tuple_d)
tuple_d[2][0] = 'b'
print(tuple_d)

# 元祖内置函数
print(tuple_a.count("a"))
print(tuple_a.count(1))
print(tuple_a.index(2))

# 集合{}
set_a = {1, 2, 3}
set_b = {1, 5, 4}

print(type(set_a))
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
set_a.add('a')
print(set_a)

# set去重
set_c = "asddsadfa"
print(set(set_c))

# 字典  空{}
dict_a = {"a": 1, "b": 2}
dict_b = dict(a=1, b=2)
print(dict_a)
print(type(dict_a))
print(dict_b)
print(type(dict_b))
print(dict_a.keys())
print(dict_a.values())
print(dict_a.pop("a"))
print(dict_a)
print(dict_a.popitem())

dict_c = {}
dict_d = dict_c.fromkeys([(1, 2, 3), "keys"])
print(dict_d)
