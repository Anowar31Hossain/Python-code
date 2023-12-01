def check_list_equal(l1, l2):
  if len(l1)!=len(l2):
    return  False
  for i in range(len(l1)):
    if l1[i]!=l2[i]:
      return False

  else:
    return True

if __name__ == "__main__":
  l1=[[1,2],[1,2,3]]
  l2=[[1,2],[1,2,3]]
  result=check_list_equal(l1,l2)
  print(result)
