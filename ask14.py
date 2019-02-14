

x = [0,0]
x[0]=int(raw_input("Enter lower limit: "))
x[1]=int(raw_input("Enter uper limit: "))
d =  int(raw_input("Enter difference: "))
a = []
for i in range(x[0],x[1]+1) :
    if (i % 2 != 0):
        a.append(i)

for i in range(0,len(a)-1) :
    if ((a[i+1] - a[i]) == d) :
        print(a[i])
        print(a[i+1])
        break
    elif ((a[i] - a[i+1]) == d) :
        print(a[i])
        print(a[i + 1])
        break



