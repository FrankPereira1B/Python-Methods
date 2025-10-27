
# Capitalising the first letter of a sentence

''' "txt" is required which any string values which will be pushed through this function
to get the required result, in this instance it is capitalising first word'''
def capitalize(txt):
    x = chr(ord(txt[0])-32)+ txt[1:]
    print(x)
    return x

''' Capitalize method without using any in built functions
    txt: text given
    chr_list = list of ascii characters for capital letters
    ord_list = list of ascii characters for small letters'''

def capitalize2(txt, chr_list, ord_list):
    x = txt[0]
    if x in ord_list:
        y = ord_list.get(x)
        z = y - 32
        print(x)
        print(y)
        print(z)
    else:
        print("No ascii character")
        
    for key, val in chr_list.items():
        if val == z:
            cap = key
            print(cap)
            txt = cap+txt[1:]
            print(txt)
    return x, y, z, cap, txt


# String creates a string of x characters with the character in the center
''' txt: Required here to pass through a string will be centred according to the length"
    n = Basically dictates length of a string'''
def center(txt, n):
    x = abs(len(txt) -n)
    txt = " "*x + txt + " "*x
    return txt
    print(txt)