f = 20
import math
def main():
    str = "Learn Python"
    print ("Hello World!!!")
    print(5*"\n")
    f = 5
    print (f)
    print (str)
    print (str[3])
    print (str[3:])
    print (str * 3)
    #print (str + f)
    list1 = [123, 3.1415, "string"]
    print (list1)
    print (list1[1])
    print (list1[0]*2)
    list1[1] = list1[1] * 2
    print (list1)
    tuple1 =(456, 2.245, "tuple", "python", "xyz")
    print (tuple1)
    print (tuple1[2])
    print (tuple1[2:4])

    x = 10.1
    y = math.floor (x)
    print (y)
    str1 = "Hello World"
    str2 = "Learn Python"
    print (str1[0:5], str2[6:12])
    print ("My name is %s and I am %d years old" % ('Anaya', 8) )
    str = input ("Enter name: ")
    print ("Hello", str)
    return
main()
'''
print ("Anaya Tanaya are the best")
var = 10
print (var)
var = 'Anu Tanu'
print (var)
print (f)
'''
'''
def Dicttry():
    Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
    Dict.update({"Sarah":9})
    #print (Dict.items())
    print("Students Name: %s" % list(Dict.items()))
Dicttry()
'''
