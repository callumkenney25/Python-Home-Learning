#this is how we change values within a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('bmw')
print(motorcycles)

motorcycles.insert(0,'ferari')
print(motorcycles)

#Deleting things from lists, e.g. someone cancelling account on web application - can remove item according to it's position in the list.
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
# the above code is demonstrating giving the popped_motorcycles a new value which is the old list without the end value. We then print the list that hasn't got the end value, and print popped_motorcycles to show we still have access to the deleted item

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

#using the value of the item rather than the position to remove it
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()} is too expensive for me")