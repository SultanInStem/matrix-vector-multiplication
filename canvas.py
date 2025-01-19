import pygame
from globals import SCREEN_SIZE
import sys
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Linear Transformations")
        self.running = True 
        self.clock = pygame.time.Clock()


    def update(self): 
        pass
    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 

    def render(self): 
        self.screen.fill((0,0,0))

        pygame.display.flip()
        self.clock.tick(60)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()