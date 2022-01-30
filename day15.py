# 2-d list and netlist for loop
nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
print(nums[1][2])

for i in range(3):
	for j in range(3):
		print(nums[i][j], end = ' ')
	print()