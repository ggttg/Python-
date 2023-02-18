class Rectangle:
    # define constructor with attributes: length and width 
    def __init__(self, length , width):
        self.length = length
        self.width = width
        
    # Create Perimeter method
    def Perimeter(self):
        return 2*(self.length + self.width)
    
    # Create area method
    def Area(self):
        return self.length*self.width   
newRectangle = Rectangle(12, 10)
print(newRectangle.Area())