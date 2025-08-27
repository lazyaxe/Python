#super() = A function used in child class(sub-class) to call methods from a parent class(base-class)
#it is similar to C++'s way of inheriting constructors from parent classes in Python
#Also can be used for "Co-operative Polymorphism" and avoid the Diamond Problem.
#super() is a mro navigator from which
class shapes:
    def __init__(self, shapeColour, isColourFilled):
        self.shapeColour = shapeColour
        self.isColourFilled = isColourFilled

class circle(shapes):
    def __init__(self, shapeColour, isColourFilled, radius=0):
        super().__init__(shapeColour, isColourFilled)#super() is used when some common arguments are within sub classes
        self.radius= float(radius)
        
class square(shapes):
    def __init__(self, shapeColour, isColourFilled, square_side=0):
        super().__init__(shapeColour, isColourFilled)
        self.square_side=float(square_side)

class triangle(shapes):
    def __init__(self, shapeColour, isColourFilled, width=0, height=0):
        super().__init__(shapeColour, isColourFilled)
        self.width = float(width)
        self.height = float(height) 

#we can use default and keyword arguments for constructors
circle1 = circle(shapeColour="Red", isColourFilled=False, radius= 69)
print(circle1.radius, "meters")
print(circle1.shapeColour)
print(f"Is shape filled ?", circle1.isColourFilled)
print()

square1 = square(shapeColour="Blue", isColourFilled=True, square_side=47)
print(square1.square_side, "meters")
print(square1.shapeColour)
print(f"Is shape filled ?", square1.isColourFilled)

triangle1 = triangle(shapeColour="Purple", isColourFilled=True, width=96, height=69 )
print(triangle1.width, "meters")
print(triangle1.height, "meters")
print(triangle1.shapeColour)
print(f"Is shape filled ?", triangle1.isColourFilled)