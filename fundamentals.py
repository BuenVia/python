#REMOVE VOWELS FROM A STRING

#Variables
msg = "This is a string and I want to remove all of the vowels"
vowels = ["a", "e", "i", "o", "u"]

#New variabale containing list() function to turn string in to a list
split_msg = list(msg)

#For every item in the split_msg list
for x in split_msg:
    #For every item in the vowels list
    for y in vowels:
        #If the item in the split_msg list is the same as any item in the vowels list
        if x == y:
            #Method to remove the item from the split_msg list
            split_msg.remove(x)
#Method to turn/ revert the split_msg list back in to a string, using the string.join() method.
print("".join(split_msg))