print("Lists")
num=[1,2,3,4,5,6,6] #dynamic size
fruit=["apple","guava","banana","grape","mango"]
mixed=[1,"hello",2,3]
empty=[]
for x in fruit:
    print(x)
print(len(num))
print(type(num))
print(num.count(6))
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

# List comprehension
ums=[85,8,96,5,89,56]
square=[x ** 2 for x in ums]
print(square)

# sort list
numb=[2,8,9,6,4,1,0,6]
print(numb)
print(len(numb))

numb.sort()
print(numb)

numb.sort(reverse=True)
print(numb)

numb=[2,8,9,6,4,1,0,6]
numb.reverse()
print(numb)

def get(n):
    return abs(n-10)
numm=[5,7,8,9,24,9,2,5]
print(numm)
numm.sort(key=abs) # sort according to their absolute value
print(numm)
fruit.sort(key=len) # sort according to their lengths
print(fruit)
numm.sort(key=get)
print(numm)

# Copy list
cube=[x**3 for x in range(5)]
print(cube,len(cube))

c1=cube.copy()
print(c1)

c2=list(cube)
print(c2)

c3=cube[:]
print(c3)

# Join lists
new_list=c1+cube
print(new_list) #or

cube.extend(c1)  #or
print(cube)

for x in c1:
    cube.append(x)  
print(cube)