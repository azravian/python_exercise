
class ComplexNum:
    
    def __init__(self, real = 0, img = 0):
        self._real = real
        self._img = img
        
    @property #set the following method as getter for real
    def real(self):
        return self._real
    
    @real.setter #sets the following methods as setter for real
    def real(self, newreal):
        self._real = newreal
        
    @real.deleter #sets the following method for attr. deletion for real
    def real(self):
        del self._real
    
    @property #set the following method as getter for img
    def img(self):
        return self._img
    
    @img.setter #sets the following methods as setter for img
    def img(self, newImg):
        self._img = newImg
        
    @img.deleter #sets the following method for attr. deletion for img
    def img(self):
        del self._img
    
    def modulus(self):
        return (self.real**2 + self.img**2)**0.5
    
    def Conjugate(self):
        #returns conjugate of complex number.
        return ComplexNum(self.real, -self.img)
    
    # Overloading string
    def __str__(self):
        return f"{self.real}+{self.img}j"
    
    # Overloading + operator
    def __add__(self, other):
        NewReal = self.real + other.real
        NewImg = self.img + other.img
        SumCompNum = ComplexNum(NewReal, NewImg)
        return SumCompNum
    
    # Overloading - operator
    def __sub__(self, other):
        NewReal = self.real - other.real
        NewImg = self.img - other.img
        SubCompNum = ComplexNum(NewReal, NewImg)
        return SubCompNum
    
    # Overloading * operator 
    def __mul__(self, other):
        # (a+bj) * (x+yj) = (a*x - b*y) + (a*y + b*x)j
        NewReal = (self.real * other.real) - (self.img * other.img)
        NewImg = (self.real * other.img) + (self.img * other.real)
        return ComplexNum(NewReal, NewImg)
    
    # Overloading div / operator
    def __truediv__(self, other):
        NewReal = ((self.real * other.real) + (self.img * other.img)) / (other.real**2 + other.img**2)
        NewImg = ((other.real * self.img) - (self.real * other.img)) / (other.real**2 + other.img**2)
        return ComplexNum(NewReal, NewImg)
    
    # Overloading // operator for modulus division
    def __floordiv__(self, other):
        return self.modulus() / other.modulus()
    
    # Overload == operator
    def __eq__(self, other):
        if self.real == other.real and self.img == other.img:
            return True
        else:
            return False
    
    #overload != Operator
    def __ne__(self, other):
        if self.real != other.real or self.img != other.img:
            return True
        else:
            return False
    
    #Overload > Operator
    def __gt__(self, other):
        if self.modulus() > other.modulus():
            return True
        else:
            return False
    
    #Overloads < operator
    def __lt__(self, other):
        if self.modulus() < other.modulus():
            return True
        else:
            return False
        
    #Overload >= Operator
    def __ge__(self, other):
        # At this point we can use ==, !=, >, and < operators as thy are already defined above
        if self > other and self == other:
            return True
        else:
            return False
    
    #Overloads <= Operator
    def __le__(self, other):
        if self < other and self == other:
            return True
        else:
            return False
