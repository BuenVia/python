#REMOVE VOWELS FROM A STRING
msg = "This is a string and I want to remove all of the vowels"
vowels = ["a", "e", "i", "o", "u"]

split_msg = list(msg)

for x in split_msg:
    for y in vowels:
        if x == y:
            split_msg.remove(x)
print("".join(split_msg))