import math
radius = float(input("Enter the radius of the circle: "))

area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
sqrt_area = math.sqrt(area)

print(f"Area of circle: {area}")
print(f"Circumference: {circumference}")
print(f"Square root of area: {sqrt_area}")
