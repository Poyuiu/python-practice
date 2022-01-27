#function
def hello():
    print("hello")
def add(num1, num2):
    ans = float(num1) + float(num2)
    print(ans)
def add_test(num1, num2):
    print(num1+num2)
num1 = input();
num2 = input();
add(num1, num2)
#add_test(num1, num2)
#notice the different between python2 and python3
def value(num1, num2):
    return 10
v = value(num1, num2)
print(v)
def none(num1, num2):
    return
v = none(num1, num2)
print(v)
