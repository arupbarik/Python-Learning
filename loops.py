print("loops")
i=0
while i<5:
    print("hello")
    i+=1
else:
    print("--------------")
for x in range(5):
    print(x)
else:
    print("--------------")
for x in range(2,10):
    print(x)
else:
    print("--------------")
for x in range(2,20,4):
    print(x)
else:
    print("--------------")
for x in range(20,0,-4):
    print(x)
else:
    print("--------------")
for y in "apple":
    print(y)
else:
    print("--------------")
# print only odd numbers in a range 
for z in range(10):
    if z%2==0:
        continue
    else:
        print(z)
else:
    print("--------------")
