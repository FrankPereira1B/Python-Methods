
# Capitalising the first letter of a sentence
def capitalize(txt):
    x = chr(ord(txt[0])-32)+ txt[1:]
    print(x)
    return x

# String creates a string of x characters with the character in the center
def center(txt, n):
    x = abs(len(txt) -n)
    txt = " "*x + txt + " "*x
    print(txt)