#  tryna solve leetcode questions though 

list = [1, 3434, 5, 676, 4, 8, 9, 10]

min_val = list[0]
max_val = list[0]

for num in list:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print("Minimum value:", min_val)
print("Maximum value:", max_val)

# 
nums = [2,7,11,5]
target = 9 
c = nums[0] + nums[1]
print(c)
index = nums.index(5)
print(index)

