import pygame
import sys
import random
pygame.init()

screen_width = 800
screen_height = 600
screen= pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
score = 3
pygame.display.set_caption("cyber_gardener")
pygame.font.init()
font = pygame.font.SysFont("Arial", 24 )
text_surface = font.render("cyber_gardener", True, (255,255,255))

class Water(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.y = 0
    def update(self):
        self.rect.y += 5
        if self.rect.y > 600:
            self.kill()
            global score; score -= 1

class Acid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((200, 0 ,0))
        self.rect = self.image.get_rect()
        self.rect.y = 0

    def update(self):
        self.rect.y += 5
        if self.rect.y > 600:
            self.kill()

SPAWN_ACID = pygame.USEREVENT +2
pygame.time.set_timer(SPAWN_ACID, 3000)
SPAWN_WATER = pygame.USEREVENT + 1
pygame.time.set_timer (SPAWN_WATER, 1500)

class Robot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,50))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= 6
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 6
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += 6
        if keys[pygame.K_d] and self.rect.right < 800:
            self.rect.x += 6

all_sprites = pygame.sprite.Group()
player = Robot()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWN_WATER:
            new_water = Water()
            new_water.rect.x = random.randint(0, screen_width - 50)
            all_sprites.add(new_water)
        if event.type == SPAWN_ACID:
            new_acid = Acid()
            new_acid.rect.x = random.randint(0, screen_width - 50)
            all_sprites.add(new_acid)
    all_sprites.update()
    hits= pygame.sprite.spritecollide(player, all_sprites, False)
    for hit in hits:
        if hit != player:
            if isinstance( hit, Water):
                score += 1
            elif isinstance( hit, Acid):
                score -=3
            hit.kill()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    score_surface = font.render(f"Score: {score}", True, (255, 255, 0))
    screen.blit(score_surface, (100, 100))


    screen.blit(text_surface, (200, 100))



    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()

