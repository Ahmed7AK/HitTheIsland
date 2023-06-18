import pygame 
from paddle import Paddle
from ball import Ball


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
        self.paddle_rect = pygame.Rect(112, 500, 128, 28)
        self.ball_rect = pygame.Rect(168, 200, 10, 15)
        self.ball_speed = {"x": 7, "y": 6}
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

        # Paddle 
        Paddle(self.screen, self.paddle_rect)
        Paddle.key_input(self.paddle_rect, 10)

        # Ball
        Ball(self.screen, self.ball_rect)
        Ball.ball_collision(self)


        pygame.display.update()
                    



game = HitTheIsland()