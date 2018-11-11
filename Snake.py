import pygame
import random
import sys
import time
Black = (0,0,0)
Red = (255,0,0)
White = (255,255,255)
Blue = (0,0,255)
Green = (0,255,0)
x = []
y = []

for i in range(50):
    x.append(0)
for i in range(50):
    y.append(0)


class food(pygame.sprite.Sprite):
    def __init__(self, color, w, h):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect()

pygame.init()
size = (1280,720)
screen = pygame.display.set_mode(size)
food_list = pygame.sprite.Group()
all_list = pygame.sprite.Group()
snake_part = pygame.sprite.Group()

foods = food(Red, 24, 24)
foods.rect.x = random.randrange(0,1256)
foods.rect.y = random.randrange(0,646)
food_list.add(foods)
all_list.add(foods)

snake = food(Green, 24, 24)
all_list.add(snake)

clock = pygame.time.Clock()
x_speed = 1
y_speed = 0

long = pygame.sprite.Group()

score = 0
die = 0
x_ = 640
y_ = 360
done = False
play_again = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                play_again = 1
                die = 0
                x_ = 640
                y_ = 360
                score = 0
            if event.key == pygame.K_x:
                done = True
    screen.fill(White)
    font1 = pygame.font.SysFont("Calibri", 100, True)
    text1 = font1.render("Game over", True, Green)
    text2 = font1.render("Push R to restart", True, Red)
    screen.blit(text2, [0, 620])
    screen.blit(text1, [50, 300])
    while play_again == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    play_again = 0
                    done = True
                if event.key == pygame.K_LEFT and y_speed != 0:
                    x_speed = -25
                    y_speed = 0
                if event.key == pygame.K_RIGHT and y_speed != 0:
                    x_speed = 25
                    y_speed = 0
                if event.key == pygame.K_UP and x_speed != 0:
                    y_speed = -25
                    x_speed = 0
                if event.key == pygame.K_DOWN and x_speed != 0:
                    y_speed = 25
                    x_speed = 0

        screen.fill(Black)
        snake.rect.x = x_ + x_speed
        snake.rect.y = y_ + y_speed

        block_list = pygame.sprite.spritecollide(snake, food_list, True)
        for i in block_list:
            score += 1
        font = pygame.font.SysFont("Calibri", 50, True)
        text = font.render("SCORE: " + str(score), True, White)
        screen.blit(text, [0, 670])

        for i in range(score - 1, 0, -1):
            x[i] = x[i - 1]
            y[i] = y[i - 1]

        x[0] = x_
        y[0] = y_

        x_ = x_ + x_speed
        y_ = y_ + y_speed
        if x_ > 1280:
            x_ = 0
        if y_ > 720:
            y_ = 0
        if x_ < 0:
            x_ = 1280
        if y_ < 0:
            y_ = 720
        for i in range(score):
            part = food(Green, 24, 24)
            part.rect.x = x[i]
            part.rect.y = y[i]
            long.add(part)
            long.draw(screen)
        bite = pygame.sprite.spritecollide(snake, long, False)
        for i in bite:
            die += 1


        all_list.draw(screen)

        if len(food_list) == 0:
            foods.rect.x = random.randrange(0, 1256)
            foods.rect.x = random.randrange(0, 646)
            food_list.add(foods)
        food_list.draw(screen)

        clock.tick(10)
        pygame.display.flip()
        for i in long:
            long.remove(i)
        if die != 0:
            play_again = 0
            break
    pygame.display.update()
pygame.quit()


