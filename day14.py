# for loop practice
# for letter in "hello":
# 	print(letter)

# for num in [0, 1, 2, 3, 4]:
# 	print(num)

# for num in range(5):
# 	print(num)
	
# for num in range(2, 6):
# 	print(num)

def power(num1, num2):
	v = 1
	for i in range(num2):
		v *= num1
	return v

num1 = input()
num2 = input()
num1 = int(num1)
num2 = int(num2)
print(power(num1, num2))