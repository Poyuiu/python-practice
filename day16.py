# your code goes here
file = open("123.txt", mode = "r")
# mode = "r" for read
# mode = "w" for write directly
# mode = "a" for write continuely
list = file.readlines()
file.close()

file = open("input.txt", mode = "w", encoding = "utf-8")
file.write("你好")
file.close()

# without close function, we could do this replaced
with open("input.txt", mode = "w") as file:
	file.write("hello")
	