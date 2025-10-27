
# Capitalising the first letter of a sentence

''' "txt" is required which any string values which will be pushed through this function
to get the required result, in this instance it is capitalising first word'''
def capitalize(txt):
    x = chr(ord(txt[0])-32)+ txt[1:]
    print(x)
    return x

# String creates a string of x characters with the character in the center
''' txt: Required here to pass through a string will be centred according to the length"
    n = Basically dictates length of a string'''
def center(txt, n):
    x = abs(len(txt) -n)
    txt = " "*x + txt + " "*x
    return txt
    print(txt)