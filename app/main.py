import pygame
from models.Player import Player
from models.Projectile import Projectile
from models.Enemy import Enemy

pygame.init()


screen_width = 700
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


bg = pygame.image.load("./Game/bg.jpg")
char = pygame.image.load("./Game/standing.png")
walkCount = 0


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    man.draw(win)
    goblin.draw(win)

    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# Main loop
run = True
fps = 27

man = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
bullets = []

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(
                Projectile(
                    round(man.x + man.width // 2),
                    round(man.y + man.height // 2),
                    6,
                    (0, 0, 0),
                    facing,
                )
            )
    if keys[pygame.K_UP]:
        man.isJump = True

    if man.isJump:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount**2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
