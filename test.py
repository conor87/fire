import pygame
import sys
from PIL import Image, ImageSequence

def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygameImage)
    return frames

class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, bottom, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = (x, bottom))
        self.image_index = 0
    def update(self):
        self.image_index += 1
        self.image = self.images[self.image_index % len(self.images)]
    
 
pygame.init()
pygame.display.set_caption('Pygame Window')  
background = pygame.image.load("media/narzedziownia.bmp")
clock = pygame.time.Clock() 
rozmiar_zdjecia = background.get_rect().size


WSIZE = (0, 0)
screen = pygame.display.set_mode(WSIZE)
W, H = screen.get_size()
print(W, H)

skala = H / rozmiar_zdjecia[1]

background = pygame.transform.scale(background, (W, rozmiar_zdjecia[1] * skala))
# img = pygame.transform.scale(img, (200, 200))
#img = pygame.transform.scale(img, (236, 167))

# screen.blit(background, [0, 0])
screen.blit(background, [0, (H - rozmiar_zdjecia[1] * skala) / 2])


gifFrameList = loadGIF('media/eee.gif')
animated_sprite = AnimatedSpriteObject(500,500,gifFrameList) 
all_sprites = pygame.sprite.Group(animated_sprite)
 

loop = 1
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = 0
 
    pygame.display.update()
    
    all_sprites.update()

    
    all_sprites.draw(screen)
    pygame.display.flip()
    
    
    
    clock.tick(20)
 
pygame.quit()
sys.exit()
