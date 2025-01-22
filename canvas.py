import pygame
from globals import SCREEN_SIZE, GRAY_COLOR, matrix_multiply, GREEN_COLOR, RED_COLOR, BLUE_COLOR, to_screen_coords
import sys
from vector import Vector
from matrix import RotationMatrix, ShearMatrix, SqueezeMatrix, StretchMatrix,  RotationShearMatrix
import math
import numpy as np
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.unit_length = 100
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Linear Transformations")
        self.running = True 
        self.is_paused = False
        self.clock = pygame.time.Clock()

        self.matrix_choice = 1
        self.basis_i = Vector(np.array([self.unit_length,0]), RED_COLOR)
        self.basis_j = Vector(np.array([0,self.unit_length]), GREEN_COLOR)
        self.prev_i = Vector(np.array([self.unit_length, 0]), RED_COLOR)
        self.prev_j = Vector(np.array([0,self.unit_length]), GREEN_COLOR)
        self.transformations = [
            RotationMatrix(0,2 * math.pi,0.01), 
            ShearMatrix(0,2,0.01), 
            SqueezeMatrix(0,1,0.01), 
            StretchMatrix(0,1,0.01), 
            RotationShearMatrix(0,math.pi,0.01)
        ]
        self.fixed_grid_lines = []
        for row in range(SCREEN_SIZE[1] // self.unit_length):
            self.fixed_grid_lines.append([[0, row * self.unit_length], [SCREEN_SIZE[0], row * self.unit_length]]) 
        for col in range(SCREEN_SIZE[0] // self.unit_length): 
            self.fixed_grid_lines.append([[col * self.unit_length, 0], [col * self.unit_length, SCREEN_SIZE[1]]])

    def reset(self): 
        self.is_paused = True
        self.matrix_choice = 1
        self.basis_i = Vector(np.array([self.unit_length,0]), RED_COLOR)
        self.basis_j = Vector(np.array([0,self.unit_length]), GREEN_COLOR)
        self.prev_i = Vector(np.array([self.unit_length, 0]), RED_COLOR)
        self.prev_j = Vector(np.array([0,self.unit_length]), GREEN_COLOR)
        for i in range(len(self.transformations)): 
            self.transformations[i].reset()
    
    def draw_fixed_cartesian(self): 
        for i in range(len(self.fixed_grid_lines)): 
            pygame.draw.aaline(
                self.screen, 
                GRAY_COLOR,
                (self.fixed_grid_lines[i][0][0], self.fixed_grid_lines[i][0][1]),
                (self.fixed_grid_lines[i][1][0], self.fixed_grid_lines[i][1][1])
            )

    def draw_dynamic_cartesian(self): 
        num_lines = 20
        origin = np.array([SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2])


    def update(self): 
        if self.is_paused: return 
        self.transformations[self.matrix_choice - 1].update()
        new_i = matrix_multiply(self.transformations[self.matrix_choice - 1].get_matrix(), self.prev_i.get_vector())
        new_j = matrix_multiply(self.transformations[self.matrix_choice - 1].get_matrix(), self.prev_j.get_vector())
        self.basis_i.set_vector(new_i)
        self.basis_j.set_vector(new_j)




    def handle_number_click(self):
        for i in range(len(self.transformations)): 
            self.transformations[i].reset()
        self.prev_i.set_vector(self.basis_i.get_vector())
        self.prev_j.set_vector(self.basis_j.get_vector())

    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_r: 
                    self.reset()
                elif event.key == pygame.K_SPACE: 
                    self.is_paused = not self.is_paused
                elif event.key == pygame.K_1: 
                    self.handle_number_click()
                    self.matrix_choice = 1
                elif event.key == pygame.K_2: 
                    self.handle_number_click()
                    self.matrix_choice = 2
                elif event.key == pygame.K_3: 
                    self.handle_number_click()
                    self.matrix_choice = 3
                elif event.key == pygame.K_4: 
                    self.handle_number_click()
                    self.matrix_choice = 4
                elif event.key == pygame.K_5: 
                    self.handle_number_click()
                    self.matrix_choice = 5



    def render(self): 
        self.screen.fill((0,0,0))
        self.draw_fixed_cartesian()
        # self.draw_dynamic_cartesian()

        self.basis_i.draw(self.screen)
        self.basis_j.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()