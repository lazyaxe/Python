#Area of Circumference and Perimeter of Circle
import math
radius=abs(float(input("Input radius of the circle: ")))#so that string is type casted into a float and float is positive
perimeter= round(2*(math.pi)*(radius))
print(f"perimeter = {perimeter} units")
area=round((math.pi)*(radius)*(radius))
print(f"area = {area} sq.units")
