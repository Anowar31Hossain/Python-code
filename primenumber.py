

def prime_number(n):
        for i in range(2, n):
            if (n % i == 0):
                return False

if __name__ == '__main__':

    n=int(input("Enter a number what you want to check prime or not prime:"))
    result=prime_number(n)
    if(n==0 or n==1 or result==True):
        print("The number is  prime.")
    else:
        print("The number is not prime.")

