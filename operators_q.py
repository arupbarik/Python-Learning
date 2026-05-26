print("questions for operators topic")
# Evaluate: 10 // 3, 10 % 3, 2 ** 3
print(10//3)
print(10%3)
print(2**3)

# What’s the difference between == and is?
x=55
print(x==55) # it checks the equality 
print(x is 55) # it check if the assign value is 55 or not.

# Write a condition that checks if a number is between 1 and 10 (inclusive).
print("please give to number to checks if a number is between 1 and 10 (inclusive)")
x=int(input())
if 1<x<=10:
    print("It is in define range")
else:
    print("It is not in define range")

# Explain short-circuit evaluation in and/or. Show with examples.
print("enter a number it is for and & or operation")
a=int(input())
if a<0 and a>-25:     #if both condition pass then i will print
    print("i am sad")  
elif a>0 or a==0:     #it will print when atleast one condition pass
    print("u have potential")
else:
    print("tera kuch na ho payega")

#  print(True + False + 2)
# out put is 3. true=1,false=0

# How does operator precedence affect a + b * c ** 2? Rewrite with explicit parentheses.
a=25
b=25
c=10
print(a + b * c ** 2)
print(a+(b*(c**2)))