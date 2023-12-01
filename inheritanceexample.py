
class shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2

    def area(self):
        print("I am area method of shape class")


class Triangle(shape):
    def area(self):
        area=.5*self.dim1*self.dim2
        print("Area of triange:",area)


class rectangle(shape):
    def area(self):
        area=self.dim1*self.dim2
        print("Area of rectangle:",area)
b=int(input("Enter dim 1:"))
c=int(input("Enter dim 2:"))
t1=Triangle(b,c)
t1.area()
t2=rectangle(b,c)
t2.area()