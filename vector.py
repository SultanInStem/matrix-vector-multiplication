import pygame
import math
from globals import to_screen_coords
class Vector: 
    def __init__(self, pos, color):
        self.pos = pos 
        self.color = color
        self.arrow_size = 20
        self.width = 3

    def draw(self, screen): 
        start_pos = to_screen_coords([0,0])
        end_pos = to_screen_coords(self.pos)
        pygame.draw.line(screen, self.color, (start_pos[0], start_pos[1]), (end_pos[0], end_pos[1]), self.width)

        angle = -math.atan2(self.pos[1], self.pos[0])

        # Calculate the points for the arrowhead
        left_arrowhead = (end_pos[0] - self.arrow_size * math.cos(angle - math.pi / 6),
                         end_pos[1] - self.arrow_size * math.sin(angle - math.pi / 6))
        right_arrowhead = (end_pos[0] - self.arrow_size * math.cos(angle + math.pi / 6),
                          end_pos[1] - self.arrow_size * math.sin(angle + math.pi / 6))

        # Draw the arrowhead
        pygame.draw.line(screen, self.color, end_pos, left_arrowhead, self.width)
        pygame.draw.line(screen, self.color, end_pos, right_arrowhead, self.width)

    def matrix_multiply(self, matrix): 
        A = [
            [0, -1], 
            [1, 0]
        ]
        # for i

