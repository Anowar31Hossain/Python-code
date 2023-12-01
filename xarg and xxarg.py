def add(*student):
    print(student)

add(101,"Anowar",3.75)

def add(*detail):
    print(detail)
    sum=0
    for num in detail:
        sum+=num
    print(sum)
add(10,20,30,40,50)

def student(**deatail):
    print(deatail)

student(id=101,name="Anowar")