
def main():
        number = int(input ("Enter a number: "))
        printtable (number)


def printtable (number):
    i = 0
    for i in range (11):
        print (int(number),"\tx\t", i, "\t=\t", number * i)
    return

main()

input ("Press any key to exit\n")
