#Main Function
def main():
    a = int(input("Enter a number: "))
    b = int (input("Enter another number: "))
    c = expfunction (a, b)
    print ("%d raised to %d :" %(a,b), c)
    str1 = "Hello"
    str2 = "World"
    str3 = concatestr(str1, str2)
    print (str3)

#Exponential Function
def expfunction (aa, ba):       #function takes int and returns int
    ca = aa ** ba
    return ca
#Concate string function
def concatestr (astr, bstr):    #function takes string and returns string
    global cstr             # define cstr as global variable
    cstr = astr + ' ' +  bstr
    return cstr

main()
print (cstr)                #print cstr (global variable)
input ("Press any key to exit ")
