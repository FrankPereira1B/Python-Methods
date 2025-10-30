
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

def capitalize2(txt):
    chr_list = {}
    ord_list = {}
    def op_lists():
        nonlocal chr_list, ord_list
        chr_list = {'A':65, 'B':66, 'C':67, 'D':68, 'E':69, 'F':70, 'G':71, 'H':72, 'I':73, 'J':74, 'K':75, 'L':76, 'M':77, 'N':78, 'O':79, 'P':80, 'Q':81, 'R':82, 'S':83, 'T':84, 'U':85, 'V':86, 'W':87, 'X':88, 'Y':89, 'Z':90}
        ord_list = {'a':97, 'b':98, 'c':99, 'd':100, 'e':101, 'f':102, 'g':103, 'h':104, 'i':105, 'j':106, 'k':107, 'l':108, 'm':109, 'n':110, 'o':111, 'p':112, 'q':113, 'r':114, 's':115, 't':116, 'u':117, 'v':118, 'w':119, 'x':120, 'y':121, 'z':122}
    
    #Activating lists for operation
    op_lists()

    # Assigning values to local variables to prevent UnboundLocalError
    y=z=cap = None
    
    x = txt[0]
    if x in ord_list:
        y = ord_list.get(x)
        z = y - 32
        print(x)
        print(y)
        print(z)   
        
        for key, val in chr_list.items():
            if val == z:
                cap = key
                print(cap)
                txt = cap+txt[1:]
                print(txt)
                break
        else:
            print("No matching case found") 
    else:
        print("No ascii character")
    return x, y, z, cap, txt

def op_lists():
    chr_list = {'A':65, 'B':66, 'C':67, 'D':68, 'E':69, 'F':70, 'G':71, 'H':72, 'I':73, 'J':74, 'K':75, 'L':76, 'M':77, 'N':78, 'O':79, 'P':80, 'Q':81, 'R':82, 'S':83, 'T':84, 'U':85, 'V':86, 'W':87, 'X':88, 'Y':89, 'Z':90}
    ord_list = {'a':97, 'b':98, 'c':99, 'd':100, 'e':101, 'f':102, 'g':103, 'h':104, 'i':105, 'j':106, 'k':107, 'l':108, 'm':109, 'n':110, 'o':111, 'p':112, 'q':113, 'r':114, 's':115, 't':116, 'u':117, 'v':118, 'w':119, 'x':120, 'y':121, 'z':122}
    return chr_list, ord_list

def capitalize3(txt):    
    #Activating lists for operation
    chr_list, ord_list = op_lists()
    x = txt[0]
    if x in ord_list:
        y = ord_list.get(x)
        z = y - 32
        print(x)
        print(y)
        print(z)   
        
        for key, val in chr_list.items():
            if val == z:
                cap = key
                print(cap)
                txt = cap+txt[1:]
                print(txt)
                break
        else:
            print("No matching case found") 
    else:
        print("No ascii character")
    return x, y, z, cap, txt

# String creates a string of x characters with the character in the center
''' txt: Required here to pass through a string will be centred according to the length"
    n = Basically dictates length of a string'''
def center(txt, n):
    x = abs(len(txt) -n)
    txt = " "*x + txt + " "*x
    return txt
    print(txt)

'''Count operation: Doing count operation in string without using 
built in method such as str.count().
txt: is passed through the function which is the main string
x: is the substring of the main string i.e. txt'''

def count(txt, x):
    cnt = 0
    for i in range((len(txt) - len(x)) + 1):
        if txt[i:i+len(x)] == x:
            cnt += 1
    return cnt

# Looking for characters that ends with the specified character
def ends_with(txt, x):
    ''' Looking for a specied item for instance in this string looking for values ending
    with specific character  - first method looks for specifc items and 
    looks for it'''
    cnt = 0
    for i in range((len(txt) - len(x)) + 1): 
        if txt[i:i+len(x)] == x:
            y = True
            break
    else: 
        z = False
        
        cnt += 1
    return y or z

# Looks for charcaters that are ending with speciic characters

def ends_with2(txt, x): 
    ''' Looking for characters ending with specific characters'''
    cnt = 0
    aa=bb=None
    for i in txt[::-1]: 
        if txt[-(len(x)):] == x:
            aa = True
            break
        else:
            bb = False
    
    cnt +=1
    return aa or bb

# Looking for tabs in string and multiplying it

def expand_tabs(txt, x):
    ''' Looking for a tab and then multiplying it with 
    specified numbers to expand tab. In python tab length
    is considered as 1 regardless how long the tab is despite 
    being multiplied by'''
    cnt = 0 
    for i in range(len(txt)): 
        if '\t' in txt: 
            '\t' * x 
        cnt += 1
    return txt
# Looking for a position of a word or a character in a string

def find(txt, word):
    x = None
    for i in range((len(txt) - len(word)) + 1):
        if txt[i:i+len(word)] == word:
            x = i
    return x