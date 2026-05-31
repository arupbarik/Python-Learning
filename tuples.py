print("Tuples")

point=(2,3)
print(point)

mixed=(1,2,"apple",5)
fruit=("apple","grape","mango","guaava")

order=tuple((1,2,3))
print(fruit,len(fruit),type(fruit))

# update the tuple
points=(2,5,6)

y=list(points)
print(y)
y.append(5)

points=tuple(y)
print(points)

points+=point
print(points)

# Unpacking
num=(125,58,71)
(r,g,b)=num
print(r)
print(g)
print(b)

cricket_player = ("Virat Kohli", "Batsman", "Right-hand bat", "India")
print(cricket_player)
(name,*details,country)=cricket_player
print(name)
print(details)
print(country)

#join two tuples
tuple1=(1,2,3)
tuple2=(4,5,6)

new=tuple1+tuple2
print(new)

new1=tuple1*2
print(new1)