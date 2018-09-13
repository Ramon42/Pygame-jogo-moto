# Pygame template - skeleton for a new pygame project
import pygame
import random
import Jogador
import Obstaculo
import FimDeJogo

WIDTH = 400
HEIGHT = 700
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
pygame.font.init()
fonte = pygame.font.SysFont('Calibri', 30)
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

resetJogo = True
jogar = True #controla estado do jogo, False indica que o jogador colidiu
indicadorPontos = fonte.render("", 1, RED)


# Game loop
while True:
    #Inicia o jogo
    if resetJogo == True:#
        spriteJogador = pygame.sprite.Group()
        pedrasSprites = pygame.sprite.Group()
        player = Jogador.Player()
        pedra = Obstaculo.Pedra()
        spriteJogador.add(player)
        pedrasSprites.add(pedra)
        pts = 0
        resetJogo = False#

    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if jogar == False:#
                jogar = FimDeJogo.reset(tela)
                resetJogo = jogar

    # Update
    pts = player.pontuacao
    if pts % 500 == 0:
        pedra1 = Obstaculo.Pedra(pedra.velocidade)
        pedrasSprites.add(pedra1)
        pts += 1

    player.pontuacao = pts
    player.pontos()

    spriteJogador.update()
    pedrasSprites.update()


    if player.colidiu(pedrasSprites, spriteJogador) or jogar == False:
        jogar = False#
        tela.fill(BLACK)
        tela.blit(indicadorPontos, (10, 60))
        pygame.draw.rect(tela, RED, (WIDTH/4, HEIGHT/2 , 200,50), 0)

    if jogar:#
        indicadorPontos = fonte.render(str(pts), 1, RED)
    # Draw / render
        tela.fill(WHITE)
        spriteJogador.draw(tela)
        pedrasSprites.draw(tela)
        tela.blit(indicadorPontos, (10, 60))
    # *after* drawing everything, flip the display
    pygame.display.flip()
