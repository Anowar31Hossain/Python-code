class employee:
    def __init__(self,name,emd,salary):
        self. name=name
        self.emd=emd
        self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Employee ID:",self.emd)
        print("Salary:$",self.salary)

class manager(employee):
    def printm(self):
        self.display()



class engineer(employee):
    def printe(self):
        self.display()

class technician(employee):
    def printt(self):
        self.display()

def main():
    Manager= manager("John Doe",101,6500)
    Engineer =engineer("Jane Smith",102,6000)
    Technician =technician("Mike Johnson",103,4500)

    Manager.printm()
    Engineer.printe()
    Technician.printt()

if __name__ == '__main__':
    main()
