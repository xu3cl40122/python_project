import pygame
""" 建立視窗"""
pygame.init()
screen=pygame.display.set_mode([400,300])
pygame.display.set_caption("myFirstGame")
clock = pygame.time.Clock()

"""建立畫布"""
canvas=pygame.Surface(screen.get_size())
canvas.convert()
canvas.fill([255,255,255])
x = 200
y = 150
ball_x = 300
ball_y = 200
"""把畫布放到視窗"""
screen.blit(canvas,[0,0])
pygame.display.update()
"""迴圈監測"""
running=True
while running:
    clock.tick(30)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 10
    elif keys[pygame.K_RIGHT]:
        x += 10
    elif keys[pygame.K_UP]:
        y -= 10
    elif keys[pygame.K_DOWN]:
        y += 10
    canvas.fill([255, 255, 255])
    pygame.draw.rect(canvas, [255, 0, 0], [x, y, 30, 30])
    pygame.draw.circle(canvas, [0, 0, 255], [ball_x, ball_y], 10)
    screen.blit(canvas, [0, 0])
    pygame.display.update()
    
    xDiff = x - ball_x
    yDiff = y - ball_y
    if abs(xDiff) < 30 and abs(yDiff) < 30 :
        x += xDiff*2
        ball_x -= xDiff*3
        y += yDiff*2
        ball_y -= yDiff*3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
    
