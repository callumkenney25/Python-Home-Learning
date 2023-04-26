twenty = list(range(1, 21)) 
print(twenty)

million = list(range(1, 1000001))
print(million)

total = sum(million)
print(total)

odd = list(range(1, 20, 2))
for number in odd:
	print(f"This is odd number {number}")

three = list(range(3, 31, 3))
print(three)

cubes = []
for value in range(1, 11):
	cubes.append(value**3)
print(cubes)

comprehension_cube = [value**3 for value in range(1, 11)]
print(comprehension_cube)