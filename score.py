import pygame.sprite
from constants import *


class Score(pygame.sprite.Sprite):
    def __init__(self):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.score = 0
        self.position = pygame.Vector2(SCREEN_WIDTH-40,30)
        self.font = pygame.font.SysFont('Comic Sans MS', 24)

    def update(self,dt):
        self.score += dt

    def draw(self, screen):
        surface = self.font.render(f'{self.score:.0f}',False,(255, 255, 255))
        text_rect = surface.get_rect()
        text_rect.center = self.position
        screen.blit(surface,text_rect)