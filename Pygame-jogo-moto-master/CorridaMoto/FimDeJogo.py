import pygame

BLACK = (0,0,0)
WIDTH = 400
HEIGHT = 700
RED = (255,0,0)

botao = pygame.Rect(WIDTH / 4, HEIGHT / 2, 200, 50)

def reset(tela):
    if pygame.mouse.get_pressed():
        x, y = pygame.mouse.get_pos()
        if botao.collidepoint(x, y):
            return True#
        return False#
