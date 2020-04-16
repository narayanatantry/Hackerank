y = int(input())
if int(y)!=1918:
    if (y % 4) == 0:
        if (y % 100) == 0:
            if (y % 400) == 0:
                print("12.09.".format(y))
            else:
                print("13.09.".format(y))
        else:
           print("12.09.".format(y))
    else:
       print("13.09.".format(y)

else:
    Y = "26.09.1918"
    print(Y)
