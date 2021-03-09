# Complete the vector class. Overload the + and * operators to support
# adding and multiplying two vectors.
# Example:
# v1 = 5i + 2j
# v2 = 2i + 3j
# v1 + v2 = 7i + 5j
# v1 * v2 = 10i + 6j

class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "{}i + {}j".format(self.x, self.y)
    
    def __repr__(self):
        return self.__str__()

v1 = Vector(5, 2)
v2 = Vector(2, 3)
v3 = Vector(3, 10)
print(v1)
print(v2)
print(v1 + v2 + v3)
print(v1 * v2)
