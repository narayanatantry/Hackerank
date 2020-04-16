import re
T = input().split(":")
l = ''.join(filter(lambda i: i.isdigit(),T[2]))#seperates the digits from DDCC
T.append(l)
ll = " ".join(re.findall("[a-zA-Z]+", T[2]))#seperates the characthers from DDCC
T.append(ll)
if T[4]=="PM":
    if T[0]==str(12):
                T[0] = str()
                print(T[0]+":"+T[1]+":"+T[3])
    else:
        T[0] = str(int(T[0])+ 12)
        print(T[0]+":"+T[1]+":"+T[3])
else :
    if T[0]==str(12):
        T[0]= "00"
        print(T[0]+":"+T[1]+":"+T[3])
    else:
        print(T[0]+":"+T[1]+":"+T[3])
