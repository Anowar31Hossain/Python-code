from abc import ABC,abstractmethod


class area(ABC):
    def __init__(self,d1,d2):
        self.d1=d1
        self.d2=d2
    @abstractmethod
    def are(self):
        pass


class rectangle(area):
    def are(self):
        Area=self.d2*self.d1
        print("The area of rectangle is :",Area)


class cir(area):
    def are(self):
        circle=3.1416*self.d1*self.d2
        print("The area of circle is:",circle)


def main():
    r=rectangle(30,40)
    r.are()
    c=cir(30,45)
    c.are()


if __name__ == '__main__':
    main()

