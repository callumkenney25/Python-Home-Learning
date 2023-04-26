message = "Hello Eric, would you like to learn some Python today?"
print(message)

first_name = "Eric"
last_name = "Fester"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}, would you like to learn Python today?")

name = "general grevious"
print(name.title())
print(name.lower())
print(name.upper())

famous_person = "Scott Fitzgerald"
quote = "'I was both within and without, simulataneously enchanted and repelled by the inexhaustable variety of life'" 
print(quote)
print(f"{quote}, was once said by {famous_person}")

second_famous = "F Scott Fitzgerald"
message = second_famous
print(f"{message}, once said {quote}")

first_name = " Eric "
last_name = " Fester "
print(first_name.lstrip())
print(f"{first_name.strip()} {last_name.strip()}, said the following: \n\t'would you like to learn Python today'")
