import math
square = input('What is the length of a side of the square in centimeters?')
square = float(square)
squarea = (square**2)
squaream = (squarea/10000)
print(f'The area of the square is: {squarea} square centimeters, or {squaream} square meters.')
length = input('What is the length of the rectangle in centimeters?')
width = input('What is the width of the rectangle in centimeters?')
length = float(length)
width = float(width)
rectangle_area = (length*width)
rectangle_area_m = (rectangle_area/10000)
print(f'The area of the rectangle is: {rectangle_area} square centimeters, or {rectangle_area_m} square meters.')
radius = input('What is the radius of the circle in centimeters?')
radius = float(radius)
r2 = (radius**2.0)
circle_area = r2*math.pi
circle_area_m = circle_area/10000
print(f'The area of the circle is: {circle_area} in square centimeters, or {circle_area_m} square meters.')
length = input('What is the length of a side in centimeters?')
length = float(length)
squarea = length**2
squaream = squarea/10000
circle_area = squarea*math.pi
circle_area_m = circle_area/10000
cube_volume = length**3
cube_volume_m = cube_volume/10000
sphere_volume = ((length**3)*math.pi)*1.333333
sphere_volume_m = sphere_volume/10000
print(f'The area of the square is: {squarea} in square centimeters, or {squaream} in square meters.')
print(f'The area of the circle is: {circle_area} in square centimeters, or {circle_area_m} in square meters.')
print(f'The volume of the cube is: {cube_volume} in square centimeters, or {cube_volume_m} in square meters.')
print(f'The volume of the sphere is: {sphere_volume} in square centimeters, or {sphere_volume_m} in square meters.')