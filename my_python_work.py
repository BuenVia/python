# 1. Numbers
#Integers (whole numbers)
print (1 + 1)
#Floating Point Numbers (decimal points)
print(2.3 + 9.8)
#mod operator (to find remainder)
print(7 % 4)
#order of operators (to perform multiple sums in equation)
print((3 + 2) * (7 - 2))

# 2. Srtings
#Text/ Characters in "quotation"
print("This is a string")
#Indexing (positioning of character - [0, 1, 2, 3] etc...)
print("Hello World"[8])
#Slicing (to return specific parts of string [start:stop:step])
print("This is a string"[2:9:2])
#Properties & Methods
#Concatenation (manipulating string using variables)
a = "with added text!"
print("This is a concatenated string " + a)
#Dot Method (. + written method/attribute)
x = "This is more text"
print(x.upper())
print(x.lower())
print(x.split())
#Print Formatting (to add in variables to string)]
#Format
print("This is the format{m}".format(m = " method"))
#f String
r = "method"
b = "but works better"
print(f"This is another {r}... but {b}!")