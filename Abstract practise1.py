from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class dog(animal):
    def speak(self):
        return "Ghau"

class cat(animal):
    def speak(self):
        return "meow"

def main():
    d=dog()
    print(d.speak())
    c=cat()
    print(c.speak())

if __name__ == '__main__':
    main()