from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')

background = transform.scale(image.load('galaxy.jpg'), (win_width,win_height))

clock = time.Clock()
FPS = 60

run = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (150,45))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 600:
            self.rect.x += self.speed
    def update_r(self):
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed

player1 = Player('platform.png', 5, 275, 0)
player2 = Player('platform.png', 5, 275, 470)

while run:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0,0))
        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
    display.update()