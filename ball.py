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
        if self.ball_rect.colliderect(self.paddle_rect) and self.ball_speed["y"] > 0:
            if abs(self.ball_rect.bottom - self.paddle_rect.top) < 100: # This basically finds the difference between both y's and if it is less than 100 which is too high but idc then the ball bounces
                self.ball_speed["y"] *= -1
            elif abs(self.ball_rect.right - self.paddle_rect.left) < 100 and self.ball_speed["y"] > 0:
                self.ball_speed["x"] *= -1
            elif abs(self.ball_rect.left - self.paddle_rect.right) < 100 and self.ball_speed["y"] < 0:
                self.ball_speed["x"] *= -1

        # Island Collisions 
        if self.ball_rect.colliderect(self.island_rect) and self.ball_speed["y"] < 0:
            if abs(self.ball_rect.top - self.island_rect.bottom) < 100: # This basically finds the difference between both y's and if it is less than 100 which is too high but idc then the ball bounces
                self.ball_speed["y"] *= -1
                self.go += 1
                print(self.go)
            elif abs(self.ball_rect.right - self.island_rect.left) < 100 and self.ball_speed["y"] > 0:
                self.ball_speed["x"] *= -1
            elif abs(self.ball_rect.left - self.island_rect.right) < 100 and self.ball_speed["y"] < 0:
                self.ball_speed["x"] *= -1
        
        
        