import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        a1=self.real+no.real
        a2=self.imaginary+no.imaginary
        ob=Complex(a1,a2)
        return ob

        
    def __sub__(self, no):
        a1=self.real-no.real
        a2=self.imaginary-no.imaginary
        ob=Complex(a1,a2)
        return ob
        
    def __mul__(self, no):
        a1=self.real*no.real-self.imaginary*no.imaginary
        a2=self.real*no.imaginary+self.imaginary*no.real
        ob=Complex(a1,a2)
        return ob

    def __truediv__(self, no):
        ob1=Complex(self.real,self.imaginary)
        ob2=Complex(no.real,-1*no.imaginary)
        mag=no.real**2+no.imaginary**2
        ob3=ob1*ob2
        ob4=Complex(ob3.real/mag,ob3.imaginary/mag)
        return ob4

    def mod(self):
        modulus=math.sqrt(self.real**2+self.imaginary**2)
        ob=Complex(modulus,0)
        return ob


    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':