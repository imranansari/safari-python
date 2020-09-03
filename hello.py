# from __future__ import braces # "dunder" for "internal" stuff

print("Hello Python World")

x = 10
print(x)
print(type(10))

x = "hello"
print(type(x))

print(type(True))
print(3.14); print(type(3.14))

print(0+1j**2); print(type(0+1j))

print('this is a quoted string with "double inside"')
print("no char, just single character string" + "x")
print("no autoconvert to string " + str(10))
x = f"Literal text {99 * 2}"
print(x)

x = 10
y = 3
print(f"x times y is {x * y}")
print(f"x divided by y is {x / y}")
print(f"x int-divided by y is {x // y}")
print(f"x mod by y is {x % y}")
print(f"3.2 has fractional part {3.2 % 1.0}")
print(123456789012345678901234567890)

x = """
and now
we have
a multi-line
string
"""

print(x)

print(3 < 7)
print(3 == 7)
print(3 != 7)
print(3 == 3)

x = "Hello"
y = "Hello"
print(f"x is y? {x is y}")
print(x == y)
y = "He"
z = y + "llo"
print(f"x is {x} y is {y}")
print(x == z)  # def __eq__, __lt__ and whole bunch more!
print(x is z)

