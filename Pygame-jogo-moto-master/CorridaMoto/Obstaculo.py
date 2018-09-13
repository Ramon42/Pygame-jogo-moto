import pygame
import random

LARGURA = 400
ALTURA = 700

BLUE = (0, 0, 255)

class Pedra(pygame.sprite.Sprite):
    def __init__(self, vel = 3.5):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(25, LARGURA - 25), 0)
        self.velocidade = vel

    def gerarPedraPosAleatoria(self):
        self.rect.y += self.velocidade
        if self.rect.top > ALTURA:
            self.rect.y = 0
            self.velocidade += 0.5
            self.rect.x = random.randrange(25, LARGURA - 25)
            self.rect.y =random.randrange(-50, ALTURA - 500)

    def update(self):
        self.gerarPedraPosAleatoria()
