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
print("This is the format {m}".format(m = "method"))
#f String
r = "method"
b = "but works better"
print(f"This is another {r}... but {b}!")

# 3. Lists = Ordered Sequence Holding Variety Of Objects
my_list = ["String", 100, 2.3]
print(my_list[2])
#Append (adding on to a list)
new_list = ['one', 'two', 'three']
new_list.append('four')
print(new_list)
#Pop (removing from a list)
new_list.pop(2)
print(new_list)
#Sort (reorder a list - must call before running)
diff_list = ['a', 'r', 'g', 'm', 'b']
num_list = [4,1,6,3]
diff_list.sort()
num_list.sort()
print(diff_list, num_list)
#Reverse (reverse a list - must call before running)
rev_list = [1,2,3,4,5]
rev_list.reverse()
print(rev_list)

# 4. Dictionaries = Unordered & Use Key:Value (doesn't need index location, use key instead)
my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict['key1'])
#Stacking (for when there is a dictionary inside a dictionary)
new_dict = {'a':123, 'b':'words', 'c':{'f':'one', 'g':'two', 'H':'three'}}
print(new_dict['c']['g'])
#Example of List inside of Dictionary Returning UpperCase
dict_list = {'1':['a', 'b', 'c'], '2':'value2'}
print(dict_list['1'][2].upper())
#Return .keys .values or .items
print(dict_list.keys())
print(dict_list.values())
print(dict_list.items())

# 5. Tuples = Similar to Lists but are immutable
t = ('a', 'b', 'c')

# 6. Sets = Unordered collections of unique elements
my_set = set()
my_set.add(1)
my_set.add(2)
print(my_set)
#Sets only return one instance of a repeated element
new_set = set([1,1,1,2,2,2,3,3,3,3,7,7,4,4,4])
print(new_set)

# 7. Booleans
t = 1 == 1
f = 1 > 2
print(t, f)

# 8. Files
