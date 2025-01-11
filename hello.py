import random

def shuffle (string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)
a = chr(random.randint(65,90))
b = chr(random.randint(65,90))
c = chr(random.randint(97,122))
d = chr(random.randint(97,122))
e = chr(random.randint(48,57))
f = chr(random.randint(48,57))
g = chr(random.randint(33,44))
h = chr(random.randint(33,44))

pasword = a+b+c+d+e+f+g+h
pasword = shuffle(pasword)
print("your random password is ",pasword)
