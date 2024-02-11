import matplotlib.pyplot as plt
import numpy as np

def draw_pifagor_tree(level, rotation_angle):    
    start_length = 1.0
    start_angle = 90.0
    plt.figure(figsize=(8, 8))
    plt.axis("equal")
    plt.axis("off")
    draw_branch(0, 0, start_length, start_angle, level, rotation_angle)
    plt.show()

def draw_branch(x, y, length, angle, level, rotation_angle):
    if level == 0:
        return
    x_end = x + length * np.cos(np.radians(angle))
    y_end = y + length * np.sin(np.radians(angle))
    plt.plot([x, x_end], [y, y_end], color="#b5270b", lw=1)

    new_length = length * 0.7
    new_angle_right = angle + rotation_angle
    new_angle_left = angle - rotation_angle
    draw_branch(x_end, y_end, new_length,  new_angle_right, level - 1,  rotation_angle)
    draw_branch(x_end, y_end, new_length,  new_angle_left,  level - 1,  rotation_angle)


if __name__ == "__main__":    
    try:
        level_of_tree = int(input("Enter the level of tree: "))
        branches_rotation_angle = float(input("Enter the branches rotation angle (in degrees): "))
        draw_pifagor_tree(level_of_tree, branches_rotation_angle)
    except ValueError:
        print("You should enter a number")
