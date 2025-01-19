import pygame
import math
from globals import to_screen_coords
class Vector: 
    def __init__(self, pos, color):
        self.pos = pos 
        self.color = color
        self.arrow_size = 5

    def draw(self, screen): 
        start_pos = to_screen_coords([0,0])
        end_pos = to_screen_coords(self.pos)
        pygame.draw.line(screen, self.color, (start_pos[0], start_pos[1]), (end_pos[0], end_pos[1]))


        dir_angle = math.atan2(self.pos[1], self.pos[0]) 
        arrow_angle = math.pi / 6 
        left_x = self.pos[0] - self.arrow_size * math.cos(dir_angle - arrow_angle)
        left_y = self.pos[1] - self.arrow_size * math.sin(dir_angle - arrow_angle)

        right_x = self.pos[0] - self.arrow_size * math.cos(dir_angle + arrow_angle)
        right_y = self.pos[1] - self.arrow_size * math.sin(dir_angle + arrow_angle) 


        pygame.draw.polygon(screen, self.color, [(self.end_x, self.end_y), (left_x, left_y), (right_x, right_y)])