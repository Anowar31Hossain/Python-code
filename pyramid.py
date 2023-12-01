
def main ():
    n=int(input("Enter row number :"))
    for row in range(1,n+1):
        for col in range(n-row):
            print(" ",end="")
        for col in range(1,2*row-1+1):
            print("*",end="")
        print()




if __name__ == '__main__':
    main()