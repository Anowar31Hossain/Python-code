def square(x):
    return x*x


list1 =[1,2,3,4,5]

result = list (map(square,list1))

print(result)



result1 = filter(lambda x :x%2==0,result)

print(result1)