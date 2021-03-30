# try:
#     num1 = 10
#     num2 = 0
#     print(num1 / num2)
# # except ZeroDivisionError:
# #     print("ZeroDivision异常")
# # except ValueError:
# #     print("ValueError异常")
# except:
#     print("ddd")
#     raise Exception("抛出异常")
# # 没有异常
# else:
#     print("ok")
# finally:
#     print("allways")


# 自定义异常
class MyException(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


raise MyException("aa", "dd")
