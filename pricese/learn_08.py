import os
# os.mkdir("testdir")
print(os.getcwd())
if os.path.exists("testdir"):
    with open("testdir/test.txt","w") as f:
        f.write("ddddd")
else:
    print("not exists")

