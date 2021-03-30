import time

print(time.asctime())
print(time.time())
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取两天前的时间
now_timestamp = time.time()
two_day_before = time.time() - 60 * 60 * 24 * 2
time_tuple = time.localtime(two_day_before)
print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))
