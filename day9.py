# if statement practice
hungry = True
if hungry:
    print("go to have dinner")

rainy = True
if(rainy):
    print("back to home")
else:
    print("go to work")

score = 100;
if(score == 100):
    print("i would give you 100 dollars")
elif score >= 80: 
    print("i would give you 80 dollars")
else:
    print("i wouldn't give you money")

rainy = False
if rainy == True and score == 100:
    print("and yes")

if rainy == True or score == 100:
    print("or yes")

rainy = not(rainy)
print (rainy)

def max_num(num1, num2, num3):
    return max(num1, num2, num3)

num1 = input("text num1")
num2 = input('text num2')
num3 = input('text num3')
print(max_num(num1, num2, num3))
