import pygame 

class Paddle:
 
    def __init__(self, screen, rect):
        self.screen = screen
        self.rect = rect
        
        Paddle.draw(self)

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)

    def key_input(paddle_rect, speed):
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_a]:
            paddle_rect.x -= speed
        if key_press[pygame.K_d]:
            paddle_rect.x += speed
        if key_press[pygame.K_LEFT]:
            paddle_rect.x -= speed
        if key_press[pygame.K_RIGHT]:
            paddle_rect.x += speed 

        if paddle_rect.x < 0:
            paddle_rect.x = 0
        if paddle_rect.x > 209:
            paddle_rect.x = 209       



