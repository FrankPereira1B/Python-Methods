
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
    '''Finding a position of a word in a string. In this mehtod, we need to pass through
    txt: String and a Word: substring of a string'''
    x = None
    for i in range((len(txt) - len(word)) + 1):
        if txt[i:i+len(word)] == word:
            x = i
    return x


# Using format method to add values or insert into String

def format_(txt, price): 
    ''' String is immutable so it is difficult add characters into a string
    I have used to locate the position of Dict characters and then interposed
    the targeted characters'''

    for i in range(len(txt)): 
        if txt[i] == "{": 
            x = i
            print(i)
        if txt[i] == "}": 
            y = i
            print(i)
            break
    a = txt[:x]
    print(a)

    b = txt[y+1:]
    print(b)

    txt = a + str(price) + b
    return txt

#Finding an index of a character

def index_(txt, x):
    ''' Looking for an index of the first charcter of the substring'''
    for i in range(len(txt)):
        if x[0] == txt[i]:
            ind = i 
            break
    return ind

# Looking to see if there both string and numeric characters in the string
def alnum_(txt):
    '''Looking for charcaters i.e. both string and numeric characters in the substring'''
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    b = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(txt)):
        if txt[i] not in a: 
            if txt[i] not in b: 
                x = False
                break
        else: 
            x = True
    return x

# Looking for characters that are only alphabetic charcaters in a string
def alpha_(txt):
    '''Looking for charcaters that are only alphabetic charcaters'''
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(txt)):
        if txt[i] not in a:  
                x = False
                break
        else: 
            x = True
    return x

# Looking for ascii characters in a string

def ascii_(txt): 
    ''' Looking for ascii charcaters in a string. I have used all ascii characters
    retrieved using string.printable function'''
    ascii_ = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']
    for i in range(len(txt)): 
        if txt[i] in ascii_: 
            x = True 
        else:
            x = False
    return x

# Looking for decimal characters in a string

def deci_(txt): 
    ''' Looking for decimal characters in a string'''
    deci_ = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    for i in range(len(txt)): 
        if txt[i] in deci_: 
            x = True 
        else: 
            x = False 
    return x
        
# Looking for digits in a string
def dgt_(txt): 
    ''' Looking for digits in a string'''
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    for i in range(len(txt)): 
        if txt[i] in digits: 
            x = True 
        else: 
            x = False 
    return x

# Looking for string characters are valid identifier

def identifier_(txt): 
    ''' Looking for characters that are valid identifier
    The first characters shouldnt be digits'''
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    for i in range(len(txt)):
        if txt[i] in digits:
            x = False 
            break
        for i in range(len(txt)): 
            if txt[i] in chars: 
                x = True 
            else:
                x = False
    return x

#  Looking to see characters in a string are lower alphabets
def lower_(txt): 
    ''' Looking for alphabets in a string are lower or not'''
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']
    for i in range(len(txt)): 
        if txt[i] in chars: 
            x = True 
        else: 
            x = False 
            break
    return x

# Checking if characters in a string are numeric or not

def numeric_(txt):
    ''' Checking if characters in a string are numeric or not'''
    numeric_letters = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(txt)): 
        if txt[i] in numeric_letters: 
            x = True
        else:
            x = False
            break
    return x 

# Looking for characters that are printable in a string

def print_char(txt): 
    ''' Looking for characters that are printable in a string'''
    printable_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
    '_', '`', '{', '|', '}', '~']
    for i in range(len(txt)): 
        if txt[i] in printable_chars:
            x = True
        else:
            x = False
            break
    return x

# Looking to see if all characters in the string are whitespces
def isspace_(txt): 
    ''' Looking for characters in a string are all whitespaces'''
    for i in range(len(txt)): 
        if txt[i] == " ": 
            x = True 
        else:
            x = False
            break
    return x

# Changing all first letters in a string to  capital letter

def title_(txt):
    ''' changing first letters of a string to capital letters'''
    chr_list = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f', 'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l', 'M':'m', 'N':'n', 'O':'o', 'P':'p', 'Q':'q', 'R':'r', 'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x', 'Y':'y', 'Z':'z'} 
    for i in range(len(txt)): 
        if txt[i] == " ": 
            z = i + 1 
            if txt[z] in chr_list.values():
                for key, value in chr_list.items():
                    if txt[z] == value:   # <-- fixed here
                        cap = key
                        new_txt = txt[:z] + cap + txt[z+1:]
                        txt = new_txt
                        break
            if new_txt[0] in chr_list.values():
                for key, value in chr_list.items():
                    if new_txt[0] == value:
                        cap = key
                        new_txt = cap + new_txt[1:]
                        break
    return new_txt


# Looking to see if all characters in a string are all CAPS

def isupper_(txt):
    ''' Looking to see if all characters in  a string are all CAPS'''
    chr_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    for i in range(len(txt)): 
        if txt[i] in chr_list: 
            x = True
        else:
            x = False
            break
    return x

##
