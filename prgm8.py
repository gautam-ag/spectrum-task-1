def main():
    character = "*"
    rows_number = 9

    mid = int((rows_number+1)/2)  # This mid equation (or logic) works equally well for setting rows for both even and odd rows_number

    for i in range(mid):
        print(" "*i + character*(2*(mid-i)-1))
    for j in range(mid-1, 0, -1):
        print(" "*(j-1) + character*(2*(mid-j) + 1))

if __name__ == "__main__":
    main()