import sys
input = sys.stdin.readline

str1 = input().strip()
idx = str1.find('x')
lst = []

if (idx != -1):
    lst = str1.split("x")
    int1 = int(lst[0])
    if lst[1] == "":
        int2 = 0
    else:
        int2 = int(lst[1])
    if (int1 == 2):
        xx = "xx"
    elif (int1 == -2):
        xx = "-xx"
    else:
        xx = str(int1 // 2) + "xx"
    if (int2 == 1):
        x = "+x"
    elif (int2 == -1):
        x = "-x"
    elif (int2 == 0):
        x = ""
    elif (int2 < 0):
        x = str(int2) + "x"
    else:
        x = "+" + str(int2) + "x"
    print(xx + x + "+W")
else:
    if (str1 == "0"):
        str1 = "W"
    elif (str1 == "1"):
        str1 = "x+W"
    elif (str1 == "-1"):
        str1 = "-x+W"
    else:
        str1 = str1 + "x+W"
    print(str1)