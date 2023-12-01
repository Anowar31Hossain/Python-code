
class employee:
    name=""
    empid=""
    salary=""
    def __init__(self,name,empid,salary):
        self.name=name
        self.empid=empid
        self.salary=salary

    def display(self):
        print("Name:",self.name)
        print("Employee ID:",self.empid)
        print("Salary:$",self.salary)

class manager(employee):
    def set(self, name, empid, salary):



a=manager("Anowar",101,200)

a.display()

