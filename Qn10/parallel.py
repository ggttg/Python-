from rectangle import Rectangle
class Parallelepipede(Rectangle):
    def __init__(self, length, width , height):
        Rectangle.__init__(self, length, width)
        self.height = height
        
    # define Volume method
    def volume(self):
        return self.length*self.width*self.height
L=int(input('Enter the length:'))   
B=int(input('Enter the breadth:'))  
H=int(input('Enter the height:'))     
myRectangle = Rectangle(L,B)
myRectangle.display()
print("----------------------------------")
myParallelepipede = Parallelepipede(L, B, 2)
print("the volume of myParallelepipede is: " , myParallelepipede.volume())