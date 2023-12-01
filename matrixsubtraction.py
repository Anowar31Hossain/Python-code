
def input_two_matrix():
  rows1=int(input("Enter row for A matrix:"))
  col1=int(input("Enter col for A matrix:"))
  rows2 = int(input("Enter row for B matrix:"))
  col2=int(input("Enter col for B matrix:"))
  matrix1=[]
  matrix2=[]
  for row in range(rows1):
    rowlist1=[]
    for col in range(col1):
      entry=int(input("Enter entry for A row {} colum {}:".format(row+1,col+1)))
      rowlist1.append(entry)
    matrix1.append(rowlist1)

  for row in range(rows2):
    rowlist2=[]
    for col in range(col2):
      entry=int(input("Enter entry for  B row  {} colum {}:".format(row+1,col+1)))
      rowlist2.append(entry)
    matrix2.append(rowlist2)
  return (matrix1,matrix2)

def print_matrix(list1,list2):
  print("A MATRIX:")
  for row in list1:
    for col in row:
      print(col,end="  ")
    print()
  print("B MATRIX:")
  for row in list2:
    for col in row:
      print(col , end="  ")
    print()

def matrix_add(list1,list2):
  if len(list1)!=len(list2):
    return 1
  for i in range(len(list1)):
    if len(list1[i])!=len(list2[i]):
      return 1

  else:
    Finalmat=[]
    for row in range(len(list1)):
      ro=[]
      for col in range(len(list1[0])):
        ro.append(list1[row][col]-list2[row][col])
      Finalmat.append(ro)
    return (Finalmat)

if __name__ == "__main__":
  list1,list2 = input_two_matrix()
  print(list1)
  print(list2)
  print_matrix(list1,list2)
  result=matrix_add(list1,list2)

  if (result==1):
    print("The subtraction of two matrix is not possible.")
  else:

    print("A-B:")
    for row in result:
      for col in row:
        print(col,end="  ")
      print()




