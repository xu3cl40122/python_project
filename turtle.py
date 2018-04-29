import pygame

def init():
    global screen, canvas, clock, sound
    global player1, x1, y1, score1
    global player2, x2, y2, score2
    global coin, coin_x, coin_y

    pygame.init()
    screen = pygame.display.set_mode([400, 240])
    pygame.display.set_caption("myFirstGame")
    clock = pygame.time.Clock()
    canvas = pygame.image.load('./Asset1_ball/bg.png')
    canvas.convert()
    #set plaer
    player1 = pygame.image.load('./Asset1_ball/sprite1.png')
    player1.convert()
    x1 = 100
    y1 = 150
    score1 = 0

    player2 = pygame.image.load('./Asset1_ball/sprite2.png')
    player2.convert()
    x2 = 300
    y2 = 150
    score2 = 0

    coin = pygame.image.load("./Asset1_ball/coin.png")
    coin.convert()
    coin_x = 200
    coin_y = 50
    
    #set sound
    pygame.mixer.init()
    pygame.mixer.music.load("./Asset1_ball/music.mp3")
    pygame.mixer.music.play(-1)
    sound=pygame.mixer.Sound("./Asset1_ball/coin.wav")

def updateScreen():
    global screen, canvas, player1, player2, coin
    global x1, y1, x2, y2, coin_x, coin_y

    screen.blit(canvas, [0, 0])
    screen.blit(player1, [x1, y1])
    screen.blit(player2, [x2, y2])
    screen.blit(coin, [coin_x, coin_y])

    pygame.display.update()


def checkUserControl():
    global x1, y1, x2, y2
    clock.tick(30)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x1 -= 5
    if keys[pygame.K_d]:
        x1 += 5
    if keys[pygame.K_w]:
        y1 -= 5
    if keys[pygame.K_s]:
        y1 += 5
    if keys[pygame.K_LEFT]:
        x2 -= 5
    if keys[pygame.K_RIGHT]:
        x2 += 5
    if keys[pygame.K_UP]:
        y2 -= 5
    if keys[pygame.K_DOWN]:
        y2 += 5

""" 主程式 """
init()
running = True
while running:
    updateScreen()
    checkUserControl()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
