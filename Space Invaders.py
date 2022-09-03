import pygame
import random
import math
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("SpaceInvaders")
icon= pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
mixer.music.load("background.wav")
mixer.music.play(-1)
playerimg=pygame.image.load("space-invaders.png")
playerx=370
playery=480
playerx_change=0

def player(playerx,playery):
    screen.blit(playerimg,(playerx,playery))
enemyimg=[]
enemyx= []
enemyy= []
enemyx_change=[]
enemyy_change=[]
no_ofenemys=6
for i in range(no_ofenemys):
    enemyimg.append(pygame.image.load("alien.png"))
    enemyx.append(random.randint(0, 375))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(5)
    enemyy_change.append(40)


bulltimg=pygame.image.load("bullet.png")
bulletx= 0
bullety= 370
bulletx_change=0
bullety_change=10
bullet_state="ready"
def bulletfire(bulletx,bullety):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulltimg,(bulletx+16,bullety+10))


def enemy(enemyx,enemyy,i):
    screen.blit(enemyimg[i],(enemyx,enemyy))
background=pygame.image.load("background.png")

def iscollosion(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt(math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2))
    if distance < 28:
        return True
    else:
        return False
score=0
font=pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10
over=pygame.font.Font("freesansbold.ttf",40)
def show_score(x,y):
    score_value=font.render("score:"+str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))
def gameover():
    g_over=over.render("GAMEOVER SCORE IS :"+str(score),True,(0,0,255))
    screen.blit(g_over,(100,250))
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type== pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                playerx_change = -6
            if event.key== pygame.K_RIGHT:
                playerx_change = 6
            if event.key==pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletsound = mixer.Sound('laser.wav')
                    bulletsound.play()
                    bulletx = playerx
                    bulletfire(bulletx, bullety)

        if event.type== pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key== pygame.K_RIGHT:
                playerx_change=0
    playerx+=playerx_change
    if playerx<=0:
        playerx=0
    if playerx>= 736:
        playerx=736
    boundaryx=bulletx
    boundryy=playery
    for i in range(no_ofenemys):
        if enemyy[i] > 445:
            for j in range(no_ofenemys):
                enemyy[j]=2000
            gameover()
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 5
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -5
            enemyy[i] += enemyy_change[i]
        collision = iscollosion(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            explosionsound = mixer.Sound('explosion.wav')
            explosionsound.play()

            bullety = 480
            bullet_state = "ready"
            if enemyx[i]<boundaryx:
                score += 1
            enemyx[i] = random.randint(0, 375)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyx[i], enemyy[i],i)

    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        bulletfire(bulletx,bullety)
        bullety-=bullety_change
    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()


