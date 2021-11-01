import pygame
import sys
 
pygame.init()
pygame.display.set_caption('Pygame Window')  
background = pygame.image.load("media/background.png") 
rozmiar_zdjecia = background.get_rect().size

img = pygame.image.load("media/fire.png") 
WSIZE = (0, 0)
screen = pygame.display.set_mode(WSIZE)
W, H = screen.get_size()
print(W, H)

skala = H / rozmiar_zdjecia[1]

background = pygame.transform.scale(background, (rozmiar_zdjecia[0] * skala, H))
# img = pygame.transform.scale(img, (200, 200))
img = pygame.transform.scale(img, (236, 167))
img.set_alpha(100)
# screen.blit(background, [0, 0])
screen.blit(background, [(W - rozmiar_zdjecia[0] * skala) / 2, 0])
screen.blit(img, [W * 0.39, H * 0.55])

clock = pygame.time.Clock()
 
loop = 1
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = 0
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
sys.exit()
