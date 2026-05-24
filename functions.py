print("function")
def add(a,b):
    return a+b
print(add(3,5))
# Default argument
def greet(name,msg="Hello!"):
    print(f"{msg}, {name}")
greet("void")
greet("void","konichiba!") # now it overrides the default msg
# keyword argument
def info(name,occupation):
    print(f"so this is {name} who is {occupation}")
info(name="void",occupation="developer")
# position argument
info("hi void","web dev")
# *args
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")
# **kargs
def my_Function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_Function("emil123", age = 25, city = "Oslo", hobby = "coding")
