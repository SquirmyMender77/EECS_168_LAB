import math
class Circle:
    def __init__(self, x, y, r):
        self.r= r
        self.x=x
        self.y=y
    def diameter(self):
        return 2*self.r
    def area(self):
        return math.pi*(self.r**2)
    def circumference(self):
        return 2*math.pi*self.r
    def dist_to_origin(self):
        return math.sqrt((self.x**2) + (self.y**2))
    def dist_to_center(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    def is_inside(self, other_circle):
        center_dist = self.dist_to_center(other_circle)
        return center_dist + self.r <= other_circle.r
    def is_overlap(self, other_circle):
        center_dist = self.dist_to_center(other_circle)
        return center_dist < (self.r + other_circle.r)
