n = int(input("Enter value :"))

#Type1
for i in range(1,n+1):                  #    *
    print(" " * (n-i),end = "")         #   ***
    print("*" * (2*i - 1))              #  ******

#Type2
for i in range(1,n+1):
    if i == n or i == 1:                # ***
        print("*"*n)                    # * *
    else:                               # ***
        print("*",end = "")
        print(" " * (n-2) ,end = "")
        print("*")