print("control flow")

# Write an if-elif-else block that prints "Even", "Odd", or "Zero".
print("Enter number to check odd or even")
x=int(input())
if x%2==0 and x!=0:
    print("even")
elif x%2!=0 and x!=0:
    print("odd")
else:
    print("zero")

# Use a for loop to print numbers 1 to 5.
print("printing numbers")
for x in range(1,6):
    print(x)

# What’s the difference between break and continue
print("example")
for a in range(60):
    if a%2==0:
        continue
    elif a==15:
        break
    else:
        print(a)

# Use a while loop to find the first number divisible by 7 greater than 50.
print("check the nummber")
i=51
while 1:
    if i%7==0:
        print(i)
        break
    i+=1

'''Explain the else clause in for and while loops. When does it execute?
ans- Refer to readme for answer.'''

# Convert this if-else to a ternary operator: if x > 0: msg = "positive" else: msg = "non-positive"
# ternary operator is nothing but using conditional statement in one line.
# it is frequently use in in simple logic in production.