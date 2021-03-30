import os
import json

root_path = os.path.dirname(os.path.dirname(__file__))
f = open(root_path + '/data/text_file', 'rt')
# print(f.read())
# print(f.readable())
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# f.close()

# with 可以不写close方法
# with open(root_path + '/data/text_file', 'rt') as s:
#     while True:
#         line = s.readline()
#         if line:
#             print(line)
#         else:
#             break

# json
# info = [{"name": "lll", "age": "15", "sex": "女"}, {"name": "ggg", "age": "1", "sex": None}]
# print("读取json文件")
# #json保存到文件
# json.dump(info, open(root_path + '/data/text_file', 'w'))
#loads 把文件加载字符串转换json
jsObj = json.load(open(root_path + '/data/text_file', 'r'))
print(jsObj)
print(type(jsObj))
print(jsObj[0]['name'])

