#filename = input("Enter filename: ")

filesize = input("enter the max file size: ")
print("The max size is %s" % (filesize))

filesizeStr = input("enter the max file size (MB): ")
fileSizeInt = int(filesizeStr)

print('Size in KB is', fileSizeInt*1024)

import math

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

a_str = input("enter a")
b_str = input("enter b")
c_str = input("enter c")



if not (check_int(a_str) and check_int(b_str) and check_int(c_str)):
    print("a, b and c must be digits")
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
    if a == 0:
        print("Its not a square equasion")
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print("brak rozwiazan")
        elif delta == 0:
            print("istnieje rozwiazanie ", -b / 2 * a)
        elif delta > 0:
            print("x1 = ", (-b - math.sqrt(delta)) / 2, '\n')
            print("x2 = ", (-b + math.sqrt(delta)) / 2)

