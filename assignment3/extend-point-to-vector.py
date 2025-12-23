import math

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def is_equal(self, second_point):
        if self.x==second_point.x and self.y==second_point.y:
            return True
        else:
            return False
        
    def info(self):
        return  f"Point: x = {self.x}, y = {self.y}"
    
    def distance(self, second_point):
        return math.sqrt((second_point.x - self.x)**2 + (second_point.y - self.y)**2)



class Vector(Point):
    def info(self):
        return f"Vector: x = {self.x}, y = {self.y}"

    def __add__(self, second_vector):
        new_vector = Vector(self.x+second_vector.x, self.y+second_vector.y)
        return new_vector
    
point1 = Point (5,7)
point2 = Point (6,8)
print ("Point1: "+ point1.info())
print ("Point2: "+ point2.info())

print ("are Point1 and Point2 equal? Answer: " + str(point1.is_equal(point2)))
print ("distance between point1 and point2: " + str(point1.distance(point2)))

vector1 = Vector(5,8)
vector2 = Vector(8,3)
print ("Vector1: " + vector1.info())
print ("Vector2: " + vector2.info())
vector3 = vector1+vector2
print ("Sum of vector1 and vector2 = " + vector3.info())
