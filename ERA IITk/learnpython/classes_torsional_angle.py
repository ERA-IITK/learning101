import math

class Points(object):
    def __init__(self, x, y, z):
        self.x,self.y,self.z=x,y,z

    def __sub__(self, no):
        ob=Points(self.x-no.x,self.y-no.y,self.z-no.z)
        return ob

    def dot(self, no):
        x1=self.x*no.x+self.y*no.y+self.z*no.z
        return x1


    def cross(self, no):
        x1=self.y*no.z-self.z*no.y
        y1=-self.x*no.z+self.z*no.x
        z1=self.x*no.y-self.y*no.x
        ob=Points(x1,y1,z1)
        return ob
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':