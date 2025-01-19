import pygame
from globals import SCREEN_SIZE, GRAY_COLOR, matrix_multiply, GREEN_COLOR, RED_COLOR
import sys
from vector import Vector

class Canvas: 
    def __init__(self): 
        pygame.init()
        self.unit_length = 100
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Linear Transformations")
        self.running = True 
        self.is_paused = False
        self.clock = pygame.time.Clock()
        self.basis_i = Vector([self.unit_length,0], RED_COLOR)
        self.basis_j = Vector([0,self.unit_length], GREEN_COLOR)
        self.t = 0

        self.shear_matrix = [
            [1, self.t], 
            [0, 1]
        ]
        self.basis_i = Vector(matrix_multiply(self.shear_matrix,self.basis_i.get_vector()), RED_COLOR)
        self.basis_j = Vector(matrix_multiply(self.shear_matrix,self.basis_j.get_vector()), GREEN_COLOR)

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
        pass
        # self.t += 0.01
        # self.basis_i = Vector(matrix_multiply(self.shear_matrix,self.basis_i.get_vector()), RED_COLOR)
        # self.basis_j = Vector(matrix_multiply(self.shear_matrix,self.basis_j.get_vector()), GREEN_COLOR)
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 

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