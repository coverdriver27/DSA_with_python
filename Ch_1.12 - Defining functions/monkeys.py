# monkey problem
import random
#function tp generate a string
# using a accumulator patten
def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]

    return res

print("Hello World")
print(generateOne(28))


