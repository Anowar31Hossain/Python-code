
 
class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram  
    def config(self):
        print("config is:",self.cpu,self.ram)




com1 = Computer('i3',16)
com2 = Computer('ryzen 3',20)


com1.config()
com2.config()

print(id(com1))
print(id(com2))