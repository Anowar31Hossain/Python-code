class student:
    roll=""
    gpa=""
    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll:{self.roll},gpa:{self.gpa}")

rahim=student(101,4.00)
rahim.display()
karin=student(102,3.50)
karin.display()




