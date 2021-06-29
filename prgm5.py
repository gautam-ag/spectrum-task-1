n=int(input("enter the numberS"))
a=0
j=2

while(a<n):
    Sum = 0
    for i in range(1, j):
        if (j % i == 0):
            Sum = Sum + i
    if (Sum == j):
        print(j)
        a=a+1
    j=j+1