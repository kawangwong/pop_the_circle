from random import randint
import pygame

height = 800
width = 800

circle_location_x = width - 50
circle_location_y = height - 50

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__() 
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 25)
        self.click_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.click_image, color, (25, 25), 25)
        pygame.draw.circle(self.click_image, (255, 255, 255), (25, 25), 25, 4)
        self.image = self.original_image 
        self.rect = self.image.get_rect(center = (x, y))
        self.clicked = False

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked 
        
        self.image = self.click_image if self.clicked else self.original_image

pygame.init()
window = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()

group = pygame.sprite.Group([
    SpriteObject(randint(0,circle_location_x), randint(0,circle_location_y), (128, 0, 0)),
    SpriteObject(randint(0,circle_location_x), randint(0,circle_location_y), (0, 128, 0)),
    SpriteObject(randint(0,circle_location_x), randint(0,circle_location_y), (0, 0, 128)),
    SpriteObject(randint(0,circle_location_x), randint(0,circle_location_y), (128, 128, 0)),
])

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 

    group.update(event_list)

    window.fill(0)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()