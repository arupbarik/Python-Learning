# WELCOME TO PYTHON LEARNING

`print("Hello World!")`
# Some imp points
* Indentation refers to the spaces at the beginning of a code line.

* Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

* Python uses indentation to indicate a block of code.

* The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

- **A Module is a single file containing Python code (functions, classes, variables). For example, if you create a file called math_utils.py, that file is a module.**

- Library is a collection of **Modules.**

- pip is a package manager to install modules,libraries,framwork etc.
# Example

``` python
    if 5 > 2:
     print("Five is greater than two!")
```
# Wrong code

``` python
    if 5 > 2:
    print("Five is greater than two!")
```

***Semicolons are optional in Python. You can write multiple statements on one line by separating them with `;` but this is rarely used because it makes it hard to read:***

- example

``` python
    print("Hello"); print("How are you?"); print("Bye bye!")
```

**Python prints on a new line by default.**

**Print Without a New Line
By default, the `print()` function ends with a new line.**

**If you want to print multiple words on the same line, you can use the end parameter:**

``` python
    print("Hello World!", end=" ")
    print("I will print on the same line.")
```
# Mix Text and Numbers
You can combine text and numbers in one output by separating them with a comma:

``` python
    print("I am", 35, "years old.")
```
# Variables
- Variables are case sensitive 
- To print text/string we can use `"` or `'`.
```python
   x = "John"
   # is the same as
   x = 'John'
```
- With the help of `type()` function we can see the variable assign data type.

**You can also use the `+` operator to output multiple variables:**
```python
   x = "Python "
   y = "is "
   z = "awesome"
   print(x + y + z)
```

**The // operator is important — in C, 7 / 2 gives 3 because both are ints. In Python, / always gives a float. Use // when you want integer division.**

**Converting between types**

`int("42")`            <!-- → 42      (string to int) -->

`float("3.14")`        <!-- → 3.14 -->

`str(100)`             <!-- '100' -->

`bool(0)`              <!-- → False   (0 is falsy, anything else is True) -->


`x=10**100`

`print(x)`  
* it is 10 to the power 100
# Data Types

| Type | Examples |
| --- | --- |
| Text Type | str |
| Numeric Types | int, float, complex |
| Sequence Types | list, tuple, range |
| Mapping Type | dict |
| Set Types | set, frozenset |
| Boolean Type | bool |
| Binary Types | bytes, bytearray, memoryview |
| None Type | NoneType |

- In Python, if a function doesn’t explicitly return anything, it returns `None` by default.

- `list` -> An ordered, mutable collection. Think of it like a dynamic array.
<!-- * Key Features:
          - Dynamic Size: You don’t need to declare the size upfront (unlike int arr[10] in C/Java). It grows/shrinks automatically.
          - Mixed Types: You can store integers, strings, and even other lists in the same list.
          - Mutable: You can change, add, or remove items after creation. -->

- `dict` -> A collection of key-value pairs. It’s implemented as a hash map under the hood.

- `tuple` -> An ordered, immutable collection. Once created, you cannot change its elements.
# I/O operations

**Input**

- To take input use `input()`.
- by default `input()` returns string so we need to change its types manually.

```python
   age=int(input("enter ur age: "))
   #for string we dont have to define the data type
```
**Output**

- To print any thint one display we use `print()`.
- `sep` and `end` are some extra parameters we can use in `print()`.
- We also use f-string to print diff data types in one line.
```python
   name="Soul"
   age=20
   percentage=79.367256
   print(f"my name is {name} and age is {age} also {percentage:.2f}")
```
- The pattern inside `{}` is always: `{value:format_spec}`. 
- Refer `format_spec` table for better under standing.
- use triple `'''`/`"""` quoates for print multiple strings in one print statement
```python
print(f"""
--- Report Card ---
Student  : {name}
Marks    : {marks:.1f} / 100
Grade    : {grade}
Result   : {"PASS" if marks >= 40 else "FAIL"}
""")
```
# Conditionals
**Ternary operator**
- ternary operator is nothing but using conditional statement in one line.
- value_if_true `if` condition `else` value_if_false

**if/elif/else statement**

- We can use `if/elif/else` statements to check multiple condition.
- `elif` is used for next condition to be check after `if` condition fails.
- if every things fail the `else` will run.
- there is also nested `if` also.

```python
    print("Enter num")
    a=int(input())
    b=int(input())
    c=int(input())
    if a>b and a>c:
        print(f"{a} is greater among {a} {b} {c}")
    elif b>c:
        print(f"{b} is greater among {a} {b} {c}")
    elif a==b==c:
        print("All are equal")
    else:
        print(f"{c} is greater among {a} {b} {c}")
```

**match statement**

- it is use when u know the outcomes.
- when u compare over only one parameter.
- it is better than use multiple `if/elif`.

```python
match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("wedsnes day")
    case 4:
        print("thrusday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
```
# Loops

**while loop**

- We have to initialize the variable before the loop.
- In `while` loop the loop will run until the condition is true.
- We have to increament the variable separetly.
- `else` is used to do something after the loop is finished.
- The `else` block in a `while` loop executes only if the loop did NOT break.

```python
i=0
while i<5:
    print("hello")
    i+=1
else:
    print("--------------")
```

**for loop**

- We don't have to initialize the variable before the loop.
- We don't have to increament the variable separetly it will do automatically.
- We can iterate over a list, string or range.
- It use `range()` to iterate over a range. It is typically starts from 0 and increament +1.
- If it is iterate over a list it's iteration no. is the elements present in the list.
- `else` is used to do something after the loop is finished.

```python
for x in range(5):
    print(x) # 0 to 4.
else:
    print("--------------")
for x in range(2,10):
    print(x) # it starts from 2 and goes to value 10 and loop will run upto 9 but after gaining 10 it will not run.
else:
    print("--------------")
for x in range(2,20,4):
    print(x)  # it starts from 2 and goes to value 20 and increament +4.
else:
    print("--------------")
for x in range(20,0,-4):
    print(x) # it starts from 20 and goes to value 0 and increament -4.
else:
    print("--------------")
for y in "apple":
    print(y)  # it will print each alphabet.
else:
    print("--------------")
```

***Example***

```python
# print only odd numbers in a range
for z in range(10):
    if z%2==0:
        continue
    else:
        print(z)
else:
    print("--------------")
```
# Functions

- In python we don't have to define return type and function type.
- use only `def` and it handles all automatically.
- Functions can send data back to the code that called them using the `return` statement.
- When a function reaches a `return` statement, it stops executing and sends the result back.
- If a function doesn't have a `return` statement, it returns `None` by default.
- You can assign default values to parameters. If the function is called without an argument, it uses the default value.
- By default, a function must be called with the correct number of arguments.
- You can send arguments with the `key = value syntax.` This way, with keyword arguments, the order of the arguments does not matter.
- When you call a function with arguments without using keywords, they are called positional arguments.
- You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
- Functions can `return` any data type, including lists, tuples, dictionaries, and more.
- In position argument u have to keep in mind the order.
- sometimes you may not know how many arguments that will be passed into your function.
- `*args` and `**kwargs` allow functions to accept a unknown number of arguments.
- If you do not know how many arguments will be passed into your function, add a `*`before the parameter name. then it recives a tuple of arguments and can be access accordingly.
- You can combine regular parameters with `*args`.
- Regular parameters must come before `*args`.
- If you do not know how many keyword arguments will be passed into your function, add two asterisks `**` before the parameter name.
- This way, the function will receive a dictionary of arguments and can access the items accordingly
- You can combine regular parameters with `**kargs`.
- Regular parameters must come before `**kargs`.
- You can use both `*args` and `**kwargs` in the same function.

*The order must be:*

1. regular parameters
2. *args
3. **kwargs
- Use `*` and `**` in function definitions to collect arguments, and use them in function calls to unpack arguments.

```python
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
```

**Recursion**
- Recursion is when a function calls itself.
- It is it self acts like a loop in function.
- Every recursive function must have two parts:

- A `recursive case` - The function calling itself with a modified argument
- A `base case` - A condition that stops the recursion
- 
- Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.
- If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes

```python
print("Recursion")

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))
# it is for check the limit of recursion
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000) # this code extend the calls to 2000.
```
# Lists

   






