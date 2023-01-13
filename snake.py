import pygame
import time
import random

 
# инициализация
pygame.init()

# цвета 
blue = (0, 0, 240)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 90)

# экран (размер)
displ_width = 400
displ_height = 400
# окно
displ = pygame.display.set_mode((displ_width, displ_height))
 
# подпись сверху
pygame.display.set_caption("SNAKE")
 
 
# snake settings
# место змеи
snake_block = 10
# скорость змеи/fps
snake_speed = 10
 
clock = pygame.time.Clock()
 
# функция для экранных сообщений
font_style = pygame.font.SysFont('bahnschrift', 25)
score_font = pygame.font.SysFont('comicsansms', 30)
 
# наша змея
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(displ, black, [x[0], x[1], snake_block, snake_block])
 
# очки
def your_score(score):
    value = score_font.render("SCORE: " + str(score), True, yellow)
    displ.blit(value, [0, 0])
 
def message(msg, color):
    # рисуем текст
    mesg = font_style.render(msg, True, color)
    # тут меняем позицию текста, если надо
    displ.blit(mesg, [displ_width / 6, displ_height / 3])
 
 
def game_loop():
    # флаг game_over
    game_over = False
    # флаг game_close
    game_close = False
 
    # coords
    x1 = displ_width / 2
    y1 = displ_height / 2
 
    x1_change = 0
    y1_change = 0
 
    # snake params
    snake_list = []
    lenght_of_snake = 1
 
    # coords для еды
    food_x = round(random.randrange(0, displ_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, displ_width - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            displ.fill(white)
            message("LOOSE, q-to quit, c-play again", red)
            your_score(lenght_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        # условия проигрыша
        if x1 >= displ_width or x1 < 0 or y1 >= displ_height or y1 < 0:
            game_close = True
 
        x1 += x1_change
        y1 += y1_change
        # заливка фона
        displ.fill(blue)
 
        # змея и еда
        pygame.draw.rect(displ, green, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
 
        if len(snake_list) > lenght_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        our_snake(snake_block, snake_list)
        pygame.display.update()
 
        # скорость змеи и ее длинна
        if x1 == food_x and y1 == food_y:
           food_x = round(random.randrange(0, displ_width - snake_block) / 10.0) * 10.0
           food_y = round(random.randrange(0, displ_height - snake_block) / 10.0) * 10.0
           lenght_of_snake += 1
        clock.tick(snake_speed)
       
        
    pygame.quit()
    quit()
 
game_loop()