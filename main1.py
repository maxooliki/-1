import pygame
import time

W, H = 1280, 720
window = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

pygame.init()
pygame.font.init()

img_back = "fon.jpg"
background = pygame.transform.scale(pygame.image.load(img_back) ,(W,H))
time_current=0
time_current=time.time()
def game():
    global time_current
    enemyGr.draw(window)

    enemy1.update()

    if time.time() -time_current >= 2:
        enemy2.update()
        if time.time() - time_current >= 4:
            enemy3.update()





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

font = pygame.font.SysFont('Arial', 48)
font1 = pygame.font.SysFont('Arial', 69)

enemyGr = pygame.sprite.Group()


# ground = pygame.sprite.Sprite()
# ground.image =pygame.transform.scale(pygame.image.load("ground.jpg"),(150,300))
speed = 4
def plus():
    global score
    global speed
    score += 1
    speed += 0.2
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


enemy1 = Enemy(1500, H/2+30, 90, 130, 'fire.png', speed)
enemyGr.add(enemy1)
enemy2 = Enemy(1500, H/2+30, 90, 130, 'fire.png', speed)
enemyGr.add(enemy2)
enemy3 = Enemy(1500, H/2+30, 90, 130, 'fire.png', speed)
enemyGr.add(enemy3)
enemy4 = Enemy(2400, H/2+30, 90, 130, 'fire.png', speed)
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
            plus()
    for cos in enemyGr:
        if cos.rect.colliderect(player):
            gameover =True

    if gameover == False:

        window.blit(background, (0, 0))
        text = font.render('Счёт: ' + str(score), 1, (0, 0, 0))
        window.blit(text, (10,10))
        all_sprites.draw(window)
        pygame.display.flip()
        game()
        pygame.display.update()
    else:
        over = font1.render('Game Over', 1, (254, 0, 0))
        window.blit(over, (W/2-120, H/2-100))
        pygame.display.update()

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
