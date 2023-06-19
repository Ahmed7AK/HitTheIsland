import pygame

class Island:
    def __init__(self, screen, rect):
        self.screen = screen
        self.rect = rect
        
        Island.draw(self)
    
    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
        pygame.draw.circle(self.screen, (0, 0, 0), ((self.rect.x, self.rect.y + self.rect.h / 2)), self.rect.h / 2)
        pygame.draw.circle(self.screen, (0, 0, 0), ((self.rect.x + self.rect.w, self.rect.y + self.rect.h / 2)), self.rect.h / 2)
