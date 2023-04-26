guest_list = ['scott fitzgerald', 'margaret atwood', 'matthew pennington', 'siakha, goddess of the sharks']
print(f"Hi {guest_list[0]}, would you like to join me for dinner?")
print(f"Hi {guest_list[-1].title()}, would you like to join me for dinner?")

guest_list = ['scott fitzgerald', 'margaret atwood', 'matthew pennington', 'siakha, goddess of the sharks']
cannot_make = 'matthew pennington'
guest_list.remove(cannot_make)
print(guest_list)
guest_list.append('umbar, of umbars star bar and bazarr')
print(guest_list)
print(f"Hello {guest_list[3].title()}, please could you attend my dance? {cannot_make.upper()} cannot make it anymore")

invitation = 'would you please attend my dinner, if you are at all free'
print(f"Hello {guest_list[0]}, {invitation}")
print(f"Hello {guest_list[1]}, {invitation}")
print(f"Hello {guest_list[2]}, {invitation}")
print(f"Hello {guest_list[3].title()}, {invitation}")

#the code below enables us to print a message for each guest in the guest list
for guest in guest_list:
	print(f"Hello {guest.title()}, {invitation}!")

extra_table = 'Good news! We have found a larger table'
for guest in guest_list: 
	print(f"{extra_table}, {guest.title()}, {invitation}")

guest_list = ['scott fitzgerald', 'margaret atwood', 'matthew pennington', 'siakha, goddess of the sharks']
next_time = guest_list.pop()
next_time = guest_list.pop()
print(next_time)
sorry = 'I apologise, however there is no longer space for you at my dinner'
print(f"{next_time.title()}, {sorry}")