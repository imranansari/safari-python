
# External tools can do static type checking :
# def add(a: int, b: int) -> int:
def add(a, b):
    """
    This is an addition method
    :param a: first operand
    :param b: second operand
    :return: sum
    """
    return a + b

print(add(2,3))
print(add.__doc__)
# print(add(2,"3"))

# functions must have parens
def show():
    print("hello")

show()

# default values with =
# variable length arguments with *
# key/value pairs iwth ** -- "keyword arguments"
def addUp(a=3, b=7, *args, **kwargs):
    print(f"a is {a}, b is {b}")
    for arg in args:
        print(f"> {arg}")
    for k,v in kwargs.items():
        print(f"key={k} has value {v}")

# can name arguments (with some restrictions :)
addUp(b=99)

# varargs
addUp(3, 2, 9, 8, 7)

# keywords: (positional args must be POSITIONAL
addUp(1,2,3,4,5,fred="Jones", jim="Smith")

print(1, 2, 3, 4, sep=",", end="")
print("more")

numbers = [1,2,3,4,5,6,7]
addUp(*numbers)  # also can spread a dictionary using **

value = 10
def show():
    value = 20  # creates a new function scoped variable
    print(value)

def update():
    # global anything is bad design :)
    global value  # also "nonlocal" -- moves up one level to the enclosing scope
    value = 20
    print(value)

show()
print(value)
print("-----")
update()
print(value)

#lambda expressions SINGLE LINE, SINGLE EXPRESSION RESULTS...
addTwo = lambda x, y: x + y

sum = addTwo(1,2)
print(sum)

names = ["Fred", "Jim", "Sheila", "Alice", "Bob"]
print(names)
names.sort(reverse=True)
print(names)
names.sort(key=lambda s: s[1])
print(names)
