import pygame

class Ball:
    def __init__(self, screen, rect):
        self.screen = screen
        self.rect = rect
        Ball.draw(self)

    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 0), (self.rect.x, self.rect.y), ((self.rect.w + self.rect.h) / 2))
    
    def ball_collision(self):
        # Initial Forces
        self.ball_rect.y += self.ball_speed["y"]
        self.ball_rect.x += self.ball_speed["x"]

        # Wall Collisions
        if self.ball_rect.y <= self.ball_rect.w + 1:
            self.ball_speed["y"] *= -1

        if self.ball_rect.x <= self.ball_rect.w + 1:
            self.ball_speed["x"] *= -1

        if self.ball_rect.x >= 337 - self.ball_rect.w - 1:
            self.ball_speed["x"] *= -1

        # Paddle Collisions 
        if self.ball_rect.colliderect(self.paddle_rect):
            self.ball_speed["y"] *= -1
 