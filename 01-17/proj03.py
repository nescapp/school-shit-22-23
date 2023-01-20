class Fraction:
    def __init__(self, num1, den1, num2, den2):
        self.num1 = num1
        self.den1 = den1
        self.num2 = num2
        self.den2 = den2

    def ajouter(self):
        return ((self.num1 * self.den2) + (self.den1 * self.num2)) / (self.den1 * self.den2)
    def soustraire(self):
        return ((self.num1 * self.den2) - (self.den1 * self.num2)) / (self.den1 * self.den2)
    def multipler(self):
        return ((self.num1 * self.num2) / (self.den1 * self.den2))
    def diviser(self):
        return ((self.num1 * self.den2) / (self.den1 * self.num2))
    def opposer(self):
        return (-self.num1 / self.den1)

test = Fraction(12, 4, 12, 4)

print(test.ajouter())
print(test.soustraire())
print(test.multipler())
print(test.diviser())
print(test.opposer())