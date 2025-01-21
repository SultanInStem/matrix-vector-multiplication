SCREEN_SIZE = (1400,800)
GRAY_COLOR = (128,128,128)
GREEN_COLOR = (144, 238, 144)
RED_COLOR = (240, 128, 128)
BLUE_COLOR = (0,71,171)

def to_math_coords(point): 
    math_x = point[0] - (SCREEN_SIZE[0] // 2)
    math_y = (SCREEN_SIZE[1] // 2) - point[1]
    return [math_x, math_y]

def to_screen_coords(point):
    screen_x = point[0] + (SCREEN_SIZE[0] // 2) 
    screen_y = (SCREEN_SIZE[1] // 2) - point[1]
    return [screen_x, screen_y]

def matrix_multiply(matrix, v): 
    ### check for compatibility later
    v_prime = [0] * len(matrix)
    for row in range(len(matrix)): 
        for col in range(len(v)): 
            v_prime[row] += matrix[row][col] * v[col]
    return v_prime

