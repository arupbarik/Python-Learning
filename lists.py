print("Lists")
num=[1,2,3,4,5] #dynamic size
fruit=["apple","guava","banana","grape","mango"]
mixed=[1,"hello",2,3]
empty=[]
for x in fruit:
    print(x)
print(len(num))
print(type(num))
print(num[1])
print(num[-1])
fruits=["apple","guava","banana","grape","mango"]
print(fruits[1:4]) # prints index 1 to 3
print(fruits[:5]) # print from start to 4 no. index
print(fruits[:]) # prints whole list
print(fruits[::2]) # prints with two increament in index
print(fruits[::-1]) # Reversed list print
# modification
nums=[1,2,3,9,4,6,85,8,96,5,89,56]

print(nums)
print(len(nums))

nums.append(100)
print(nums)
print(len(nums))

nums.insert(1,10)
print(nums)
print(len(nums))

nums.remove(56)
print(nums)
print(len(nums))

remove_item=nums.pop(11)
print(nums)
print(len(nums))
print(remove_item)

# nums.pop()
# print(nums)  # it will remove the last element of the list
# print(len(nums))

del nums[11]
print(nums)
print(len(nums))

nums.clear()
print(nums)
print(len(nums))

# 
