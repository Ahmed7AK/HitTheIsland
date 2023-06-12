import pygame 
from paddle import Paddle


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
        self.paddle_rect = pygame.Rect(112, 500, 100, 28)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        
        # Loop
        self.running = True
        while self.running:
            self.clock.tick(self.FPS)
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
                    break
            HitTheIsland.draw(self)

    def draw(self):
        self.screen.fill(self.WHITE)
        Paddle(self.screen, self.paddle_rect)
        Paddle.key_input(self.paddle_rect, 15)
        pygame.display.update()
                    



game = HitTheIsland()