# num2=int(input("Enter a number:"))   zero division error
# result=20/num2
# print(result)
# print("Done")
# text="Anowar"
# print(text[10])  #Index error
# try:
#     list=[20,0,30]
#     result=list[0]/list[3]
#     print(result)
#     print("Done")

# except ZeroDivisionError:
#     print("Dividing by zero is not possible.")
# except IndexError:
#     print("Index Error")
# finally:
#     print("successful")

# try:
#     num1=int(input("Enter first number:"))
#     num2=int(input("Enter second number:"))
#     result=num1/num2
#     print(result)
# except (ValueError):
#     print("You have to insert only integer.")
# except ZeroDivisionError:
#     print("You do not divided something by using zero")   # it is use this system except (ZeroDivisionError,ValueError,IndexError):
# except (IndexError):
#     print("you insert wrong index.")
# finally:
#     print("Thanks!")

def voter (age):
    if age<18:
        raise ValueError("Invalid voter!")
    return "you are allowed to vote!"

try:
    print(voter(19))

except ValueError as e:
    print(e)