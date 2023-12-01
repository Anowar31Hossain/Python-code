"""
This code defines an abstract base class called “Polygon” using the ABC (Abstract Base Class)
module in Python. The “Polygon” class has an abstract method called “noofsides” that needs to
be implemented by its subclasses. There are four subclasses of “Polygon” defined:
“Triangle,” “Pentagon,” “Hexagon,” and “Quadrilateral.” Each of these subclasses overrides
the “noofsides” method and provides its own implementation by printing the number of sides it
has. In the driver code, instances of each subclass are created, and the “noofsides” method
is called on each instance to display the number of sides specific to that shape.
"""
from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def noofside(self):
        pass

class Triangle(polygon):
    def noofside(self):
        print("I have 3 sides.")

class Pentagon(polygon):
    def noofside(self):
        print("I have 5 sides.")

class Hexagon(polygon):
    def noofside(self):
        print("I have 6 sides.")

class Quadrilateral(polygon):
    def noofside(self):
        print("I have 4 sides.")

def main():
    t=Triangle()
    t.noofside()
    p=Pentagon()
    p.noofside()
    h=Hexagon()
    h.noofside()
    q=Quadrilateral()
    q.noofside()
if __name__ == '__main__':
    main()