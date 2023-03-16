import pygame

WIDTH = 600
HEIGHT = 400
FPS = 60

game_sc = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Работа с изображениями')

image = pygame.image.load('images/car.bmp')
image.set_colorkey([255, 255, 255])

car_down = pygame.transform.flip(image, False, True)
car_left = pygame.transform.rotate(image, 90)
car_right = pygame.transform.rotate(image, -90)

background =pygame.image.load('images/sand.jpg')

background = pygame.transform.scale(background, [640, 400])

finish = pygame.image.load('images/finish.png')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    game_sc.blit(background, [0, 0])
    game_sc.blit(car_right, [0, 0])
    game_sc.blit(finish, [300, 324])
   
    pygame.display.update()
    clock.tick(FPS)