
def main():
    n=int(input("How many number:"))
    first=0
    second=1
    list1=[]
    list1.append(first)
    list1.append(second)
    print(first ,second, end=" ")
    for i in range(2,n):
        fibo=first+second
        print( fibo, end=" ")
        list1.append(fibo)
        first=second
        second=fibo

    print()
    print(list1)
    num=int(input("Enter a number:"))
    for i in range(0,n+1):
        if(i==num):
            print("The fibonacci number  what you want to search:",list1[i-1])


if __name__ == '__main__':
    main()














