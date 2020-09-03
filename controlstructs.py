# conditional, using if

x = 99
if x < 50:
    print("x looks small to me")
elif x < 100:
    print("x is intermediate")
else:
    print("hmm, not small")
    print("x is largish")

print("Done with condition")

# No "switch"
# sometimes "fudged" using dict?

# while is most basic
x = 3
while x > 0:
    # pass
    print(x)
    x -= 1

print("loop done")

names = ["Fred", "Jim", "Sheila"]
for n in names:
    print(f"name is {n}")
print("loop done")

x = range(1, 22, 3)
print(x)
print(type(x))
for v in x:
    print(v)

print("-------------")

x = 3

y = "small" if x < 10 else "larger"  # same as ? :
print(y)