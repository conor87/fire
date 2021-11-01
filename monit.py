import pygame 
pygame.init()  
pygame.display.set_caption('Pygame Window')  
background = pygame.image.load("media/background.png") 
img = pygame.image.load("media/fire.png") 
background = pygame.transform.scale(background, (500, 500))
img = pygame.transform.scale(img, (200, 200))
display = pygame.display.set_mode((500, 500))
display.blit(background, [0, 0])
display.blit(img, [150, 150])
pygame.display.update() 
while True:
  pass
