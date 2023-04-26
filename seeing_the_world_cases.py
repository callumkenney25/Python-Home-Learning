dream = ['japan', 'finland', 'italy', 'mexico', 'canada']
print(dream)
print(sorted(dream))
print(f"{dream[0].title()}")

reverse_sorted = sorted(dream, reverse=True)
print(reverse_sorted)

guest_list = ['scott fitzgerald', 'margaret atwood', 'matthew pennington', 'siakha, goddess of the sharks']
for guest in guest_list:
	print(f"Hello, {guest}, we are expecting to invite {len(guest_list)} people to our party")

languages = ['Python', 'Java', 'C++', 'Ruby']
print("Original list:", languages)
languages.sort()
print("Sorted list:", languages)
languages.sort(reverse=True)
print("Sorted List (in-place, reverse)", languages)
sorted_languages = sorted(languages)
print(sorted_languages)
print(languages)