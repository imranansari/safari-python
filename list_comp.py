values = [ x for x in range(1, 10)]
print(values)
print(type(values))

print([ x * x for x in range(1, 10)])
print([ x * x for x in range(1, 10) if x % 2 == 0 ])

print([ (x, y) for x in range(1, 10) for y in range(1, x) ])
