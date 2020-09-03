names = ["Fred", "Jim", "Sheila"]
print(names)
print(type(names))
print(names[0])
names[1] = "Jimmy"
print(names)

print("Fred" in names)
print("Albert" not in names)
names.append("Alice")  # pop is "opposite" of append
print(names)
names.extend(["Albert", "William"])
print(names)

print(names[1:4])
print(names[0:5:2])
print(names[::])  # clone the list...
newlist = names[::]
print(names is newlist)
print(names[::-1])
print(f"length of names is {len(names)}")

del names[3]
print(names)

a = 3
b = 2
print(f"{a}, {b}")
del b
# print(f"{a}, {b}")
b = None  # kinda "null"

print(b)
print(type(b))
print(str(None))
# b.doStuff()

tup = 1, "Hello", 9.2
print(tup)
print(type(tup))
print(tup[0])
# tuples are immutable
# tup[0] = 99

tup2 = (tup, "more", 123)
print(tup2)
print(len(tup2))

names.extend(tup2)
print(names)

n2 = {"Fred": "Jones", "Alice": "Smith"}
print(n2)
print(type(n2))
print(n2["Fred"])
print("---------------")
print(n2.keys())
print("---------------")
print(n2.values())
print("---------------")
print(n2.items())

print(True and True)  # logical and/or should use the English word.. & | are bitwise
print(True and False)
print(True or False)
# xor comes from library called operator
from operator import xor
print(xor(True, False))
print(xor(True, True))


