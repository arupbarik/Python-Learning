# Python Learning Documentation

A complete, structured guide to learning Python from beginner to advanced level, with practical examples and a study path.

## 1. What Is Python?

Python is a high-level, interpreted programming language known for:
- Clear and readable syntax
- Fast development speed
- Rich standard library
- Strong ecosystem for web, automation, data science, AI, scripting, and tooling

## 2. Why Learn Python?

Python is useful for:
- Web development (Django, Flask, FastAPI)
- Automation and scripting
- Data analysis (Pandas, NumPy)
- Machine learning and AI (scikit-learn, PyTorch, TensorFlow)
- APIs and backend systems
- DevOps and system tooling

## 3. Setup and First Program

Install Python 3 from the official site and verify:

```bash
python --version
# or
python3 --version
```

Run your first program:

```python
print("Hello, World!")
```

## 4. Python Fundamentals

### 4.1 Syntax and Indentation

- Python uses indentation to define code blocks.
- Standard indentation is 4 spaces.
- Indentation is required, not optional.

```python
if 5 > 2:
    print("Five is greater than two")
```

### 4.2 Comments

```python
# Single-line comment

"""
Multi-line comment style using a triple-quoted string.
Usually used as a docstring.
"""
```

### 4.3 Variables and Naming

- Variables are dynamically typed.
- Names are case-sensitive.
- Use snake_case for variables and functions.

```python
name = "Arup"
age = 20
is_student = True
```

### 4.4 Data Types

| Category | Types |
| --- | --- |
| Text | str |
| Numeric | int, float, complex |
| Sequence | list, tuple, range |
| Mapping | dict |
| Set | set, frozenset |
| Boolean | bool |
| Binary | bytes, bytearray, memoryview |
| Null | NoneType |

### 4.5 Type Conversion

```python
x = int("42")
y = float("3.14")
z = str(100)
b = bool(0)   # False
```

### 4.6 Input and Output

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")
```

Useful `print` arguments:
- `sep`: separator between values
- `end`: ending character instead of newline

## 5. Operators

### 5.1 Arithmetic
`+`, `-`, `*`, `/`, `%`, `//`, `**`

### 5.2 Comparison
`==`, `!=`, `>`, `<`, `>=`, `<=`

### 5.3 Logical
`and`, `or`, `not`

### 5.4 Assignment
`=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`

### 5.5 Identity and Membership
- Identity: `is`, `is not`
- Membership: `in`, `not in`

## 6. Control Flow

### 6.1 if / elif / else

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
```

### 6.2 Ternary Expression

```python
status = "Adult" if age >= 18 else "Minor"
```

### 6.3 match-case (Python 3.10+)

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid day")
```

## 7. Loops

### 7.1 while loop

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### 7.2 for loop

```python
for x in range(5):
    print(x)  # 0 to 4
```

### 7.3 break, continue, pass

```python
for n in range(10):
    if n == 3:
        continue
    if n == 8:
        break
    print(n)
```

### 7.4 Loop else

`else` runs if loop ends normally (not with `break`).

## 8. Functions

### 8.1 Defining and Calling

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

### 8.2 Parameters

- Positional arguments
- Keyword arguments
- Default parameters
- Variable-length args: `*args`, `**kwargs`

```python
def intro(name, city="Unknown"):
    print(name, city)
```

### 8.3 Scope

- Local scope
- Global scope (`global` keyword)
- LEGB rule (Local, Enclosing, Global, Built-in)

### 8.4 Lambda Functions

```python
square = lambda x: x * x
print(square(5))
```

### 8.5 Recursion

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

## 9. Strings

- Immutable sequence of characters
- Supports indexing and slicing

```python
text = "Python"
print(text[0])      # P
print(text[1:4])    # yth
print(text[::-1])   # nohtyP
```

Common methods:
- `upper()`, `lower()`, `title()`, `strip()`
- `split()`, `join()`
- `find()`, `replace()`
- `startswith()`, `endswith()`

## 10. Lists

- Ordered, mutable, allows duplicates

```python
nums = [1, 2, 3]
nums.append(4)
nums.insert(1, 10)
nums.remove(2)
```

### 10.1 Slicing

```python
arr = [10, 20, 30, 40, 50]
print(arr[1:4])   # [20, 30, 40]
```

### 10.2 List Comprehension

```python
squares = [x * x for x in range(6)]
```

### 10.3 Sorting and Copying

- Sort: `sort()`, `sorted()`
- Reverse: `reverse()`
- Copy: `copy()`, slicing `[:]`, `list(original)`

## 11. Tuples

- Ordered, immutable, allows duplicates

```python
point = (10, 20)
```

### 11.1 Packing and Unpacking

```python
person = ("Alex", 25, "India")
name, age, country = person
```

## 12. Dictionaries

- Key-value mapping, mutable, insertion-ordered

```python
student = {"name": "John", "age": 18}
print(student["name"])
student["age"] = 19
```

Useful methods:
- `get()`, `keys()`, `values()`, `items()`
- `update()`, `pop()`, `popitem()`, `clear()`

## 13. Sets

- Unordered, unique elements

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
```

## 14. File Handling

Use `with` to manage files safely.

```python
with open("files.txt", "r", encoding="utf-8") as f:
    data = f.read()

with open("files.txt", "a", encoding="utf-8") as f:
    f.write("\nNew line")
```

Modes:
- `r`: read
- `w`: write (overwrite)
- `a`: append
- `x`: create new file
- `b`: binary mode
- `t`: text mode (default)

## 15. Error Handling

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("Valid number", x)
finally:
    print("Always executes")
```

Use `raise` to throw custom exceptions.

## 16. Object-Oriented Programming (OOP)

Core ideas:
- Class and object
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")
```

## 17. Modules, Packages, and pip

- Module: a Python file (`.py`) with code.
- Package: a directory of modules (usually with `__init__.py`).
- Install libraries with `pip`.

```bash
pip install requests
```

```python
import math
print(math.sqrt(25))
```

## 18. Useful Built-in Functions

Important built-ins to master:
- `len()`, `type()`, `id()`
- `sum()`, `min()`, `max()`, `sorted()`
- `range()`, `enumerate()`, `zip()`
- `map()`, `filter()`, `any()`, `all()`
- `abs()`, `round()`

## 19. Intermediate Python Topics

### 19.1 Iterators and Generators

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

### 19.2 Comprehensions

- List comprehension
- Dictionary comprehension
- Set comprehension

```python
squares = {x: x * x for x in range(5)}
```

### 19.3 Decorators

Decorators wrap and extend function behavior.

### 19.4 Context Managers

`with` statements and custom context managers for safe resource handling.

### 19.5 Dataclasses

Use `@dataclass` to reduce boilerplate for classes storing data.

## 20. Advanced Python Topics

- Virtual environments (`venv`)
- Type hints and static checking (`typing`, `mypy`)
- Testing with `unittest` and `pytest`
- Logging with `logging` module
- Regular expressions (`re`)
- Concurrency:
  - `threading`
  - `multiprocessing`
  - `asyncio`
- Performance basics and profiling
- Packaging and publishing (`setuptools`, `pyproject.toml`)

## 21. Coding Best Practices

- Follow PEP 8 style guidelines.
- Write meaningful variable/function names.
- Keep functions small and single-purpose.
- Add docstrings for reusable code.
- Handle exceptions intentionally.
- Prefer readability over clever tricks.
- Write tests for critical logic.

## 22. Learning Path (Recommended Order)

1. Syntax, variables, data types, I/O
2. Operators and conditionals
3. Loops and control statements
4. Functions and recursion
5. Strings, lists, tuples, dicts, sets
6. File handling and exceptions
7. OOP
8. Modules, packages, and external libraries
9. Intermediate features (generators, decorators, dataclasses)
10. Testing, typing, async/concurrency, packaging

## 23. Repository Topic Map

This repository already includes practice files for many fundamentals:

- Variables: `var.py`, `varq.py`
- Input/Output: `i_o.py`
- Operators: `operators_q.py`
- Conditionals: `conditional.py`, `control_flow_q.py`
- Loops: `loops.py`
- Functions: `functions.py`, `functionq.py`
- Recursion: `recusion.py`
- Strings: `strings.py`, `stringq.py`
- Lists: `lists.py`
- Tuples: `tuples.py`
- Dictionaries: `dict.py`
- Sets: `sets.py`
- File handling: `file_i_o.py`, `files.txt`
- Command notes: `commands.txt`

## 24. Practice Strategy

For each topic:
1. Read concept + syntax
2. Run examples manually
3. Modify examples with your own inputs
4. Solve at least 5 small exercises
5. Build one mini-project per 3-4 topics

Mini-project ideas:
- Calculator app (I/O, conditionals, loops, functions)
- Student grade manager (lists/dicts/functions/files)
- Expense tracker (file handling + data structures)
- CLI contact book (CRUD with dictionaries and files)

## 25. Quick Revision Checklist

- Can you explain mutable vs immutable types?
- Can you use slicing and comprehensions confidently?
- Do you know when to use list vs tuple vs set vs dict?
- Can you write reusable functions with proper parameters?
- Can you handle errors using `try/except`?
- Can you read/write files safely with `with open(...)`?
- Can you create and use classes with inheritance?
- Can you import modules and install packages?

## 26. Next Milestones

After finishing this repository, continue with:
- DSA in Python (arrays, strings, stacks, queues, trees, graphs)
- API development with FastAPI/Flask
- SQL + Python integration
- Testing and CI workflows
- One portfolio project end-to-end

## 27. Advanced Python and Ecosystem Map

### 27.1 Advanced Python Topics to Learn

- Memory model and internals: references, mutability, garbage collection
- Iteration protocol: iterables, iterators, custom iterator classes
- Generators: `yield`, generator expressions, lazy pipelines
- Decorators in depth: function decorators, class decorators, `functools.wraps`
- Context managers: `with`, custom context managers, `contextlib`
- Descriptors and properties: `property`, descriptor protocol
- Dunder methods: `__str__`, `__repr__`, `__len__`, `__iter__`, operator overloading
- Dataclasses and attrs-style modeling
- Type hints: `typing`, `TypeVar`, `Generic`, `Protocol`, `TypedDict`
- Async programming: event loop, coroutines, `async`/`await`, async context managers
- Concurrency patterns: threads vs processes vs async I/O
- Testing architecture: unit, integration, mocking, fixtures, parametrization
- Packaging and distribution: wheels, versioning, `pyproject.toml`, publishing
- Performance tuning: profiling, caching, vectorization, memory optimization

### 27.2 Web Development

- Django: full-featured web framework with ORM, auth, admin, templating
- Flask: lightweight microframework for APIs and small web apps
- FastAPI: modern high-performance API framework with type hints and auto docs
- SQLAlchemy: powerful ORM and SQL toolkit
- Alembic: database migrations for SQLAlchemy projects
- Pydantic: runtime data validation and schema modeling
- Celery: background task queue and distributed workers

### 27.3 Data Analysis and Visualization

- NumPy: n-dimensional arrays and numerical computing foundation
- Pandas: tabular data processing, cleaning, and analysis
- Polars: high-performance DataFrame engine for large datasets
- Matplotlib: core plotting library
- Seaborn: statistical visualization with simpler high-level APIs
- Plotly: interactive plots and dashboards

### 27.4 AI and Machine Learning

- scikit-learn: classical ML models, preprocessing, and evaluation
- XGBoost: gradient boosting for structured/tabular data
- LightGBM: efficient gradient boosting for large datasets
- CatBoost: boosting library strong with categorical features
- PyTorch: deep learning framework with dynamic computation graphs
- TensorFlow/Keras: deep learning framework and high-level APIs
- Hugging Face Transformers: pre-trained NLP and multimodal transformer models
- Optuna: hyperparameter optimization and experiment tuning

### 27.5 Data Engineering and Big Data

- Apache Spark (PySpark): distributed data processing and ETL at scale
- Dask: parallel/distributed arrays and DataFrames in Python
- Airflow: workflow orchestration and scheduled pipelines
- Prefect: modern workflow orchestration with Python-first design
- dbt (Python ecosystem integration): analytics engineering and SQL transformations

### 27.6 Cybersecurity and Networking

- Scapy: packet crafting, sniffing, and protocol analysis
- Requests: HTTP client for scripts and security tooling
- httpx: modern sync/async HTTP client
- Paramiko: SSH automation and remote command execution
- pwntools: exploit development and binary interaction toolkit
- cryptography: secure encryption, signing, and key operations
- python-nmap: integration with Nmap scanning results
- YARA Python bindings: malware pattern matching workflows

### 27.7 Automation, DevOps, and System Scripting

- subprocess and pathlib (standard library): process control and filesystem automation
- Fabric: remote execution and deployment scripting over SSH
- Ansible (Python ecosystem): infrastructure automation and configuration management
- Click/Typer: building robust command-line applications
- Rich/Textual: rich terminal UI, logs, tables, and interactive CLIs

### 27.8 Testing, Quality, and Tooling

- pytest: modern testing framework with fixtures and plugins
- unittest: standard library testing framework
- hypothesis: property-based testing
- mypy/pyright: static type checking
- ruff/flake8/pylint: linting and code quality rules
- black: automatic code formatter
- isort: import sorting and formatting
- pre-commit: run quality checks before each commit

### 27.9 Desktop, Bots, and Other Domains

- Tkinter/PySide/PyQt: desktop GUI applications
- Selenium/Playwright: browser automation and web testing
- BeautifulSoup/lxml: HTML parsing and web scraping
- Scrapy: scalable scraping framework
- python-telegram-bot/discord.py: chatbots and community automation

### 27.10 How to Choose a Stack by Goal

- For backend/API: FastAPI + SQLAlchemy + Alembic + Pydantic
- For data analysis: NumPy + Pandas + Matplotlib/Seaborn
- For ML projects: Pandas + scikit-learn + Optuna, then PyTorch
- For cybersecurity scripting: Requests/httpx + Scapy + Paramiko + cryptography
- For automation tools: Typer + Rich + subprocess + pathlib

---

Every line you debug is proof your hard work is turning into skill. 😊
