import pygame
from globals import SCREEN_SIZE, GRAY_COLOR, matrix_multiply, GREEN_COLOR, RED_COLOR
import sys
from vector import Vector
from matrix import RotationMatrix, ShearMatrix, SqueezeMatrix, StretchMatrix,  RotationShearMatrix
import math
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
        self.basis_i = Vector([self.unit_length,0], RED_COLOR)
        self.basis_j = Vector([0,self.unit_length], GREEN_COLOR)
        self.prev_i = Vector([self.unit_length, 0], RED_COLOR)
        self.prev_j = Vector([0,self.unit_length], GREEN_COLOR)
        self.transformations = [
            RotationMatrix(0,2 * math.pi,0.01), 
            ShearMatrix(0,2,0.01), 
            SqueezeMatrix(0,2,0.01), 
            StretchMatrix(0,2,0.01), 
            RotationShearMatrix(0,math.pi,0.01)
        ]

    def reset(self): 
        self.is_paused = True
        self.matrix_choice = 1
        self.basis_i = Vector([self.unit_length,0], RED_COLOR)
        self.basis_j = Vector([0,self.unit_length], GREEN_COLOR)
        self.prev_i = Vector([self.unit_length, 0], RED_COLOR)
        self.prev_j = Vector([0,self.unit_length], GREEN_COLOR)
        for i in range(len(self.transformations)): 
            self.transformations[i].reset()

    def draw_fixed_catesian(self): 
        for row in range(0, SCREEN_SIZE[1] // self.unit_length): 
            pygame.draw.aaline(
                self.screen, 
                GRAY_COLOR, 
                (0, row * self.unit_length),
                (SCREEN_SIZE[0], row * self.unit_length)
            )
        for col in range(0, SCREEN_SIZE[0] // self.unit_length): 
            pygame.draw.aaline(
                self.screen, 
                GRAY_COLOR, 
                (col * self.unit_length, 0),
                (col * self.unit_length, SCREEN_SIZE[1])
            )

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
        self.draw_fixed_catesian()

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