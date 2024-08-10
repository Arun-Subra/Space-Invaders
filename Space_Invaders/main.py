import pygame
from pygame import mixer
import random as r
import time

#Initialise
pygame.init()

#Create window
screen = pygame.display.set_mode((800, 600))

#Create background
background = pygame.image.load('background.jpg')

#Music
mixer.music.load('background.wav')
mixer.music.play(-1)
#Title and Icon
pygame.display.set_caption("Space Invaders UwU")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def showScore(x, y, value):
    score = font.render("Score: " + str(value), True, (0, 255, 0))
    screen.blit(score, (x, y))

#Game Over
bigFont = pygame.font.Font('freesansbold.ttf', 64)

def gameOver():
    over_text = bigFont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


#Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 368
playerY = 480
player_speed = 0.5
playerX_change = 0
captured = False #if enemy has touched player

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 6
enemy_speed = 1

for i in range(num_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(r.randint(0, 736))
    enemyY.append(r.randint(50, 200))
    enemyX_change.append(r.choice([enemy_speed, - enemy_speed]))
    enemyY_change.append(40)

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bullet_speed = 0.3
bulletY_change = 2
bullet_fired = False

#Add player to screen
def player(x, y):
    screen.blit(playerImg, (x, y))

#Add enemy to screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fireBullet(x, y):
    screen.blit(bulletImg, (x + 16, y + 32))
    
def hasCollided(x1, y1, x2, y2):
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    return True if distance <= 30 else False


# Game loop
running = True
while running:
    screen.fill((0, 0, 255))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #Keystrokes
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = - player_speed
            elif event.key == pygame.K_RIGHT:
                playerX_change = player_speed
            elif event.key == pygame.K_SPACE:
                if not bullet_fired:
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    bullet_fired = True
                    bulletX = playerX

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and playerX_change < 0:
                playerX_change = 0
            elif event.key == pygame.K_RIGHT and playerX_change > 0:
                playerX_change = 0

    #Move player    
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    
    for i in range(num_enemies):

        if hasCollided(enemyX[i], enemyY[i], playerX, playerY):
            mixer.music.load('curb.wav')
            mixer.music.play(-1)
            captured = True
        if captured:
            for j in range(num_enemies):
                enemyY[j] = 2000
            gameOver()
            break
        #Move enemy
        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX[i] = 0
            enemyX_change[i] = enemy_speed
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX[i] = 736
            enemyX_change[i] = - enemy_speed
            enemyY[i] += enemyY_change[i]

        if hasCollided(enemyX[i], enemyY[i], bulletX, bulletY) and bullet_fired:
            hitSound = mixer.Sound('explosion.wav')
            hitSound.play()
            bullet_fired = False
            bulletY = 480
            score_value += 1
            if score_value % 10 == 0:
                enemy_speed += 0.5
            enemyX[i] = r.randint(0, 736)
            enemyY[i] = r.randint(50, 200)

        enemy(enemyX[i], enemyY[i], i)

    #Move bullet if fired
    if bullet_fired:
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY <= 0:
            bullet_fired = False
            bulletY = 480
    
    #Increase enemy speed
    player(playerX, playerY)
    showScore(textX, textY, score_value)
    pygame.display.update()