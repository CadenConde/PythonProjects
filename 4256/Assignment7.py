
class Point:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        
    def midpoint(self, point):
        newX = ((self.x+point.x)/2)
        newY = ((self.y+point.y)/2)
        return Point(newX,newY)
