print("Strings")

a="hello"
b='world'
print(a+" "+b)

print(a[2])
for x in a:
    print (x)

# Slicing
greet="Hello,World!"
print(greet[2:6])
print(greet[2:9])
print(greet[:6])
print(greet[2:6:2])
print(greet[::3])
print(greet[:])
print(greet[::-1])

# Methods
s="hello,arbaa"
print(s)

print(s.upper())

print(s.index("l"))

s.replace("l","v")
print(s)