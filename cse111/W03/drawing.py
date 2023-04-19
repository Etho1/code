# Ethan Spencer 1/20
# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as es_draw_sky and es_draw_ground here.
    es_draw_sky(canvas, scene_width, scene_height, split)

    es_draw_ground(canvas,scene_width,scene_height)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# es_draw_sky and es_draw_ground here.
def es_draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="springGreen3")
    es_draw_rock(canvas, scene_width, scene_height, 10, 25)

    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    es_draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    tree_center_x = 600
    tree_bottom = 70
    tree_height = 220
    es_draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    
    tree_center_x = 300
    tree_bottom = 130
    tree_height = 120
    es_draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    tree_center_x = 450
    tree_bottom = 70
    tree_height = 400
    es_draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

split = 165

def es_draw_sky(canvas, scene_width, scene_height, split):
    draw_rectangle(canvas, 0, split, scene_width, scene_height, outline='royalblue1', fill='royalblue1')
    draw_clouds(canvas, scene_width, scene_height, 10, 25)


def draw_clouds(canvas, scene_width, scene_height, min_diam, max_diam):
    for i in range(80):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(350, scene_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter * 4, y + diameter * 2, fill="ghostWhite", outline = 'ghostWhite')
    


def es_draw_pine_tree(canvas, center_x, bottom, height):

    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")
def es_draw_rock(canvas,scene_width,scene_height,min_diam,max_diam):
    for i in range(15):
            x = random.randint(0, scene_width - max_diam)
            y = random.randint(0, 150)
            diameter = random.randint(min_diam, max_diam)
            draw_oval(canvas, x, y, x + diameter *1.3, y + diameter, fill="ivory4", outline = 'ivory4')
# Call the main function so that
# this program will start executing.
main()