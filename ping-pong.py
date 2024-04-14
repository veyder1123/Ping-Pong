from pygame import *
from random import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')

background = transform.scale(image.load('galaxy.jpg'), (win_width,win_height))

clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 36)
font = font.SysFont('Arial', 80)

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()

run = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def update_l(self):
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 550:
            self.rect.x += self.speed
    def update_r(self):
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 550:
            self.rect.x += self.speed

player1 = Player('platform.png', 5, 275, 0, 145, 50)
player2 = Player('platform.png', 5, 275, 470, 145, 50)
ball = GameSprite('ball.png', 0, 160, 200, 50, 50)

speed_x = 4
speed_y = 4

score1 = 0
score2 = 0

while run:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0,0))
        text_1 = font1.render('Счёт первого игрока: '+str(score1), 1, (255,255,255))
        window.blit(text_1, (10, 20))
        text_2 = font2.render('Счёт второго игрока: '+str(score2), 1, (255,255,255))
        window.blit(text_2, (10, 50))
        ball.reset()
        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.colliderect(player1.rect) or ball.colliderect(player2.rect):
            speed_y *= -1
        if ball.rect.y < 5 or ball.rect.y > 450:
            speed_y *= -1
        if ball.rect.x > 650 or ball.rect.x < 5:
            speed_x *= -1
        if ball.rect.y > 450:
            score1 += 1
        if ball.rect.y < 5:
            score2 += 1
        if score1 >= 5:
            win = font.render('Игрок 1 победил!!!', True, (255, 255, 255))
            window.blit(win, (100, 150))
            finish = True
        if score2 >= 5:
            win = font.render('Игрок 2 победил!!!', True, (255, 255, 255))
            window.blit(win, (100, 150))
            finish = True
    else:
        finish = False
        score1 = 0
        score2 = 0
        time.delay(5000)
        player1 = Player('platform.png', 5, 275, 0, 145, 50)
        player2 = Player('platform.png', 5, 275, 470, 145, 50)
        ball = GameSprite('ball.png', 0, 160, 200, 50, 50)
    display.update()