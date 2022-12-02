class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y

p1 = Points(1, 2)
p2 = Points(3, 4)
p3 = Points(5, 6)
p4 = Points(7, 8)
p5 = Points(9, 10)

print(p1.get_x(), p1.get_y())
print(p2.get_x(), p2.get_y())
print(p3.get_x(), p3.get_y())
print(p4.get_x(), p4.get_y())
print(p5.get_x(), p5.get_y())
