def find3Numbers(a, arr_size, sum):
    # Fix the first element as a[i]
    for i in range(0, arr_size - 2):

        # Fix the second element as a[j]
        for j in range(i + 1, arr_size - 1):

            # Now look for the third number
            for k in range(j + 1, arr_size):
                if a[i] + a[j] + a[k] == sum:
                    print("Triplet is", a[i],
                          ", ", a[j], ", ", a[k])
                    return True

    # If we reach here, then no triplet was found
    return False

# Driver program to test above function
a=list(map(int, input("enter the elements").split()))
sum = int(input("enter the sum to be taken"))
arr_size = len(a)
find3Numbers(a, arr_size, sum)
