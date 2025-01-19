import pygame
from globals import SCREEN_SIZE, to_screen_coords
import sys
from vector import Vector
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Linear Transformations")
        self.running = True 
        self.clock = pygame.time.Clock()
        self.fixed_basis = Vector([0,100], (255,255,255))

    def draw_fixed_catesian(self): 

        pygame.draw.line(
            self.screen, 
            (255,255,255), 
            (0, SCREEN_SIZE[1] // 2), 
            (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2),
            2
        )

        pygame.draw.line(
            self.screen, 
            (255,255,255), 
            (SCREEN_SIZE[0] // 2, 0), 
            (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 
            2
        )
    def update(self): 
        pass
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 

    def render(self): 
        self.screen.fill((0,0,0))

        # self.vector.draw(self.screen)
        self.draw_fixed_catesian()

        pygame.display.flip()
        self.clock.tick(60)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()