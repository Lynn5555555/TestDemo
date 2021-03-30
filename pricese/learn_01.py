# 数字 int  float complex
int_a = 1
float_a = 1.2
complex_a = 2j

print(int_a)
print(float_a)
print(complex_a)

# 字符串
a = 'string&&&&\n'
print(a)
print("------")
# 转义符
a = 'string&&&&\\n'
print(a)
print("------")
# 忽略转义符 r
a = r'string&&&&\\n'
print(a)
print("------")
# 多字符串连接
a = "aaaa"
b = "dddd"

print(a + b)
print("aaa" "bbbb")
# 引用
a = "aaaa"
b = f"dddd{a}"
print(b)

print(b.format(a))

d = "ccc{x}{y}"
print(b.format(x=a, y=b))

# list
list_a = [1, 2, 3, "s"]
print(list_a[0])
print(list_a[-1])
'''不包括下标3'''
print(list_a[0:3])
