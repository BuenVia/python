newList = ["apples", "bananas", "tofu", "cats"]

def list_string(spam):
    if len(spam) == 1:
        return spam[0]
    return "{}, and{}".format(", ".join(spam[:-1]), spam[-1])

list_string(newList)