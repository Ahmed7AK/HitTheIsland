import pygame 

class HitTheIsland:
    def __init__(self):

        # Screen
        self.screen_size = (337, 600)
        self.screen = pygame.display.set_mode(self.screen_size)

        # Title and Icon
        pygame.display.set_caption("Hit The Island")
        # Icon

        # Variables 
        self.WHITE = (255, 255, 255)

        # Loop
        self.running = True
        while self.running:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
                    break
            HitTheIsland.draw(self)

    def draw(self):
        self.screen.fill(self.WHITE)
        pygame.display.update()
                    



game = HitTheIsland()