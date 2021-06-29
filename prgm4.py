def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x

# Driver Code

a=list(map(int, input("enter the elements").split()))
num1 = a[0]
num2 = a[1]

gcd = find_gcd(num1, num2)

for i in range(a[0], len(a)):
    gcd = find_gcd(gcd, a[a])

print(gcd)


