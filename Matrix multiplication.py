def input_two_list():
    rows1=int(input("Enter A matrix rows:"))
    col1=int(input("Enter A matrix colum:"))
    rows2 = int(input("Enter B matrix rows:"))
    col2=int(input("Enter B matrix colum:"))
    list1=[]
    list2 = []

    for row in range(rows1):
        rowlist1=[]
        for col in range(col1):
            entry1=int(input("Enter for A matrix row {} and colum {}:".format(row+1,col+1)))
            rowlist1.append(entry1)
        list1.append(rowlist1)

    for row in range(rows2):
        rowlist2 = []
        for col in range(col2):
            entry2 = int(input("Enter for B matrix row {} and colum {}:".format(row + 1, col + 1)))
            rowlist2.append(entry2)
        list2.append(rowlist2)
    return (list1,list2)
def print_matrix(list1,list2):
    print("A:")
    for row in list1:
      for col in row:
        print(col,end="  ")
      print()
    print("B:")

    for row in list2:
      for col in row:
        print(col, end="  ")
      print()

def multiplication_matrix(list1,list2):
    if len(list1[0])==len(list2):
        product_matrix = []
        for row in range(len(list1)):
            rowlist3=[]
            for col in range(len(list2[0])):
                product=0
                for k in range(len(list1[0])):
                    product+=list1[row][k]*list2[k][col]
                rowlist3.append(product)
            product_matrix.append(rowlist3)
        return (product_matrix)
    else:
        return 0



if __name__ == '__main__':
    list1,list2=input_two_list()
    print(list1)
    print(list)
    print_matrix(list1,list2)
    result=multiplication_matrix(list1,list2)
    if (result==0):
        print("Multiplication error:Because A matrix colum and B matrix row not equal.")
    else:
        print("A*B:")
        for row in result:
            for col in row:
                print(col,end="  ")
            print()


