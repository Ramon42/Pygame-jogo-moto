import pygame

LARGURA = 400
ALTURA = 700
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
mt = "moto.png"
moto = pygame.image.load(mt)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = moto.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA / 2, ALTURA - 50)
        self.moverX = 0
        self.moverY = 0
        self.pontuacao = 0

    def mover(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_LEFT]:
            self.moverX = -8

        if tecla[pygame.K_RIGHT]:
            self.moverX = 8

        if self.rect.right >= LARGURA:
            self.moverX = 0
            self.rect.x -= 1
        if self.rect.left <= 0:
            self.moverX = 0
            self.rect.x += 1

        if tecla[pygame.K_UP]:
            self.moverY = -8
        if tecla[pygame.K_DOWN]:
            self.moverY = 8
        if self.rect.bottom >= ALTURA:
            self.moverY = 0
            self.rect.y -= 1
        if self.rect.top <= 0:
            self.moverY = 0
            self.rect.y += 1

    def attPosicao(self):
        self.mover()

        self.rect.x += self.moverX
        self.moverX = 0
        self.rect.y += self.moverY
        self.moverY = 0

    def update(self):
        self.attPosicao()

    def pontos(self):
        self.pontuacao += 1

    def colidiu(self, obstaculo, player):
        return pygame.sprite.groupcollide(obstaculo, player, False, True)