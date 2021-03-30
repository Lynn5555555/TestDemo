class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"name:{self.name}")

    def drink(self):
        print(f"name:{self.name} 我在喝")


xiao = Person("xiao", 10)
hong = Person("hong", 15)

print(xiao.name)
print(xiao.eat())
