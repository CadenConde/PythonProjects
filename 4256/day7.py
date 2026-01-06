class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #1
    def __str__(self):
        if self.a == 0 and self.b == 0:
            return "0"
        if self.a == 0:
            return f"{self.b}i"
        if self.b == 0:
            return f"{self.a}"
        sign = "+" if self.b > 0 else "-"
        return f"{self.a} {sign} {abs(self.b)}i"
    
    #2
    def add(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    
    #3
    def negate(self):
        return Complex(-self.a, -self.b)
    
    #4
    def subtract(self, other):
        return self.add(other.negate())
    
    #5
    def multiply(self, other):
        a, b, c, d = self.a, self.b, other.a, other.b
        return Complex(a * c - b * d, a * d + b * c)
    
    #6
    def conjugate(self):
        return Complex(self.a, -self.b)
    #6
    def inverse(self):
        denom = self.a ** 2 + self.b ** 2
        return Complex(self.a / denom, -self.b / denom)
    
    #7
    def divide(self, other):
        numer = self.multiply(other.conjugate())
        denom = other.a ** 2 + other.b ** 2
        return Complex(numer.a / denom, numer.b / denom)

    #8
    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)