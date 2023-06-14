import pygame

W, H = 1280, 720
window = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

pygame.init()
pygame.font.init()

img_back = "fon.png"
background = pygame.transform.scale(pygame.image.load(img_back) ,(W,H))

def game():
    enemyGr.draw(window)
    enemyGr.update()


player = pygame.sprite.Sprite()
player.image =pygame.transform.scale(pygame.image.load("stiv.png"),(130,280))
player.rect = player.image.get_rect(center=(150, 235))
all_sprites = pygame.sprite.Group([player])

y, vel_y = player.rect.bottom, 0
vel = 5
ground_y = 520
acceleration = 10
gravity = 0.2
score = 0
textX = 50
textY = 50

font = pygame.font.Font('ImpactRegular.ttf', 48)

enemyGr = pygame.sprite.Group()

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Hello Привет', True,
                  (180, 0, 0))



window.blit(text1, (10, 50))

# ground = pygame.sprite.Sprite()
# ground.image =pygame.transform.scale(pygame.image.load("ground.jpg"),(150,300))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        x_old = self.rect.x
        y_old = self.rect.y
        keys = pygame.key.get_pressed()
        self.rect.x -= self.speed
    def draw(self, win):
        win.blit(self.image, self.rect)


enemy1 = Enemy(500, H/2+30, 90, 130, 'fire.png', 4)
enemyGr.add(enemy1)
enemy2 = Enemy(850, H/2+30, 90, 130, 'fire.png', 4)
enemyGr.add(enemy2)
enemy3 = Enemy(1500, H/2+30, 90, 130, 'fire.png', 4)
enemyGr.add(enemy3)
enemy4 = Enemy(2400, H/2+30, 90, 130, 'fire.png', 4)
enemyGr.add(enemy4)

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, W)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
rect = pygame.Rect(40, 40, 120, 120)



gameover = False
run = True
while run:
    clock.tick(100)
    acc_y = gravity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if vel_y == 0 and event.key == pygame.K_SPACE:
                acc_y = -acceleration
    for enemy in enemyGr:
        if enemy.rect.x <= 0:
            enemy.rect.x = W
    for cos in enemyGr:
        if cos.rect.colliderect(player):
            gameover =True

    if gameover == False:

        window.blit(background, (0, 0))
        all_sprites.draw(window)
        pygame.display.flip()
        game()
        pygame.display.update()
    else:
        pass
    keys = pygame.key.get_pressed()
    player.rect.centerx = (player.rect.centerx + (keys[pygame.K_d] - keys[pygame.K_a]) * vel) % 1200
    player.rect.bottom = round(y)
    vel_y += acc_y
    y += vel_y
    if y > ground_y:
        y = ground_y
        vel_y = 0
        acc_y = 0



pygame.quit()
exit()
