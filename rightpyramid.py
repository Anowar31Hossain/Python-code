def main():
    n=int(input("Enter row number:"))
    for row in range(n+1):
        for col in range((row+1),1,-1):
            print("*",end="")
            print(" ",end="")
        print()



if __name__ == '__main__':
    main()