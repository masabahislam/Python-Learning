a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("Hello")
print('Hello')


#slicing
b = "Hello, World!"
print(b[2:5])

#uppercase
a = "Hello, World!"
print(a.upper())

#lowercase
a = "Hello, World!"
print(a.lower())


#remove whitespaces
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#replace strings
a = "Hello, World!"
print(a.replace("H", "J"))

#split
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
