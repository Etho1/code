import math

def compute_area_square(side_length):
    '''computes area of a square'''
    area = side_length ** 2
    return area
def compute_area_rectangle(side_length, side2_length):
    '''computes area of a rectangle'''
    area = side_length * side2_length
    return area
def compute_area_circle(radius):
    '''computes the area of a circle'''
    area = (math.pi)*(radius ** 2)
    return area
radius = float(input('What\'s the radius of your circle?'))
area_circle = compute_area_circle(radius)
print(area_circle)

side_rectangle1 = float(input('What\'s the height of your rectangle? '))
side_rectangle2 = float(input('What\'s the length of your rectangle? '))
area_rectangle = compute_area_rectangle(side_rectangle1, side_rectangle2)
print(area_rectangle)

side_square = float(input('What\'s the length of the side of your square? '))
area_square = compute_area_square(side_square)
print(area_square)