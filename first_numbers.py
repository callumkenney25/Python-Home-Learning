for value in range(1, 5):
	print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)
#in this code we create an empty list called 'squares' - we then tell Python to loop the values from 1 through to 10. Inside the loop, the current value is raised to the second power and assigned the variable 'square'. At line 13, each new value of square is appended to the list 
#squares

cubes = []
for value in range(1, 11):
	cubes.append(value**3)
print(cubes)

squares = [value**2 for value in range(1, 11)]
print(squares)