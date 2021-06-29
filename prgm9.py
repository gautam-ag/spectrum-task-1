def kthSmallest(a, n, k):
    # Sort the given array
    a.sort()

    # Return k'th element in the
    # sorted array
    return a[k - 1]


# Driver code
if __name__ == '__main__':
    a = list(map(int, input("enter the elements").split()))
    n = len(a)
    k = int(input("enter the integer "))
    print("K'th smallest element is",
          kthSmallest(a, n, k))
