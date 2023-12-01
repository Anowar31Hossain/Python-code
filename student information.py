class student:
    def __init__(self,name,roll,cgpa):
        self.name=name
        self.roll=roll
        self.cgpa=cgpa

    def display(self):
        print(f"Name:{self.name} Roll:{self.roll} CGPA:{self.cgpa}")

class Anowar(student):
    def printa(self):
        print("Anowar Information:")
        self.display()



class Tanim(student):
    def printt(self):
        print("Tanim Information:")
        self.display()

class Shihab(student):
    def prints(self):
        print("Shihab Information:")
        self.display()
class Chand(student):
    def printc(self):
        print("Chand Information:")
        self.display()
class Nafish(student):
    def printn(self):
        print("Nafish Information:")
        self.display()

def main():
    a=Anowar("Anowar",2104031,4.00)
    t=Tanim("Tanim",2104035,4.00)
    s=Shihab("Shihab",2104032,3.55)
    c=Chand("Chand",2104033,4.00)
    n=Nafish("Nafish",2104031,3.00)
    a.printa()
    t.printt()
    s.prints()
    c.printc()
    n.printn()

if __name__ == '__main__':
    main()