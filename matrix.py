def main ():
  rows=int(input("Enter rows number for A:"))
  cols=int(input("Enter cols number for A:"))
  matrixlist=[]
  for row in range(rows):
    rowlist = []
    for col in range(cols):
      entry=int(input(f"Enter entry for row {row+1} and col {col+1}:".format(row+1,col+1)))
      rowlist.append(entry)
    matrixlist.append(rowlist)


  rows1=int(input("Enter rows number for B:"))
  cols1=int(input("Enter cols number for B:"))
  matrixlist1=[]
  for row in range(rows1):
    rowlist1 = []
    for col in range(cols1):
      entry1=int(input(f"Enter entry for row {row+1} and col {col+1}:".format(row+1,col+1)))
      rowlist1.append(entry)
    matrixlist1.append(rowlist)
  print("A:")
  for row in matrixlist:
    for item in row:
      print(item, end=" ")
    print()
  print("B:")
  for row in matrixlist1:
    for item1 in row:
      print(item1, end=" ")
    print()


if __name__ == '__main__':
  main()






