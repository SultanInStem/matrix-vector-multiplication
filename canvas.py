import pygame
from globals import SCREEN_SIZE, GRAY_COLOR, matrix_multiply, GREEN_COLOR, RED_COLOR
import sys
from vector import Vector
from matrix import Matrix, RotationMatrix, ShearMatrix
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


        self.matrix_choice = 2
        self.basis_i = Vector([self.unit_length,0], RED_COLOR)
        self.basis_j = Vector([0,self.unit_length], GREEN_COLOR)
        self.transformations = [
            RotationMatrix(0,math.pi,0.3), 
            ShearMatrix(0,2,0.01)
        ]




    def reset(self): 
        self.is_paused = True
        self.basis_i = Vector([self.unit_length,0], RED_COLOR)
        self.basis_j = Vector([0,self.unit_length], GREEN_COLOR)
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

        match(self.matrix_choice): 
            case 1: 
                self.transformations[0].update()
                new_i = matrix_multiply(self.transformations[0].get_matrix(), [100, 0])
                new_j = matrix_multiply(self.transformations[0].get_matrix(), [0, 100])
                self.basis_i.set_vector(new_i)
                self.basis_j.set_vector(new_j)
            case 2: 
                self.transformations[1].update()
                new_i = matrix_multiply(self.transformations[1].get_matrix(), [100, 0])
                new_j = matrix_multiply(self.transformations[1].get_matrix(), [0, 100])
                self.basis_i.set_vector(new_i)
                self.basis_j.set_vector(new_j)

            case __: 
                pass

    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_r: 
                    self.reset()
                elif event.key == pygame.K_SPACE: 
                    self.is_paused = not self.is_paused
                elif event.key == pygame.K_1 and self.is_paused: 
                    ### rotation matrix 
                    pass


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