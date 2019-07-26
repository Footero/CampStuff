import pygame

import random

import time



def draw_apple(apple_X,apple_Y):
    pygame.draw.rect(display, player_color,pygame.Rect(apple_X, apple_Y,10,10))
def draw_death(death_X,death_Y):
    pygame.draw.rect(display, death_color,pygame.Rect(death_X, death_Y,20,20))    
def generate_apple():
    apple_X = random.randint(2,89) * 10
    apple_Y = random.randint(2,89) * 10
    return apple_X, apple_Y
def generate_death():
    death_X = random.randint(4,86) * 10
    death_Y = random.randint(4,86) * 10
    return death_X, death_Y
def collision_with_death(death_X, death_Y):
    if snake_head[0] == death_X and snake_head[1] == death_Y or snake_head[0] == death_X + 10 and snake_head[1] == death_Y + 10 or snake_head[0] == death_X and snake_head[1] == death_Y + 10 or snake_head[0] == death_X + 10 and snake_head[1] == death_Y:
        return 1
    return 0
def collision_with_apple(snake_head,apple_X,apple_Y,grow,score,speed,death_X,death_Y):
    if snake_head[0] == apple_X and snake_head[1] == apple_Y:
        apple_X, apple_Y = generate_apple()
        death_X, death_Y = generate_death()
        grow = True
        pygame.display.set_caption("Snake game             Your score is: " + str(score))
        score += 1
        speed += 2
    return apple_X, apple_Y, grow, score, speed, death_X, death_Y

def collision_with_boundaries(snake_head):

    # if snake is outside of boundaries snap back
    if snake_head[0] > 900:
        snake_head[0] = -10
    if snake_head[0] < -10:
        snake_head[0] = 900
    if snake_head[1] > 900:
        snake_head[1] = -10
    if snake_head[1] < -10:
        snake_head[1] = 900
        
def collision_with_self(snake_head, snake_position):
    for position in snake_position[1:]:
        if snake_head[0] == position[0] and snake_head[1] == position[1]:
            return 1
    return 0
def generate_snake(snake_head, snake_position, button_direction,grow):

    #uses button_direction to decide where snake head will go

    if button_direction == 1:
        snake_head [0] += 10
    elif button_direction == 0:
        snake_head [0] -= 10
    elif button_direction == 3:
        snake_head [1] -= 10
    elif button_direction == 2:
        snake_head [1] += 10    
    snake_position.insert(0,list(snake_head))
    if grow != True:
        snake_position.pop()
    return snake_position


def display_snake(snake_position):

    #uses list of snake's positions to display snake
    for position in snake_position:
        pygame.draw.rect(display, player_color, pygame.Rect(position[0],position[1],10,10))
def play_game(snake_head, snake_position, button_direction,score,speed):

    crashed = False
    grow = False
    apple_X,apple_Y = generate_apple()
    death_X,death_Y = generate_death()

    while crashed is not True:

        for event in pygame.event.get():

            #ends game if you click on X
            if event.type == pygame.QUIT:
                crashed = True

            #sets variable used to move snake using arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    button_direction = 0
                elif event.key == pygame.K_RIGHT:
                    button_direction = 1
                elif event.key == pygame.K_UP:
                    button_direction = 3
                elif event.key == pygame.K_DOWN:
                    button_direction = 2                    


        #moves snake position
        snake_position = generate_snake(snake_head, snake_position, button_direction, grow)
        grow = False



        #display background and snake
        display.fill(window_color)
        display_snake(snake_position)
        draw_apple(apple_X,apple_Y)
        draw_death(death_X,death_Y)
        pygame.display.update()
        apple_X, apple_Y, grow, score, speed, death_X, death_Y = collision_with_apple(snake_head, apple_X, apple_Y, grow, score, speed, death_X, death_Y)

        #ends game loop if snake leaves the boundary
        if collision_with_death(death_X, death_Y) == 1:
            crashed = True
        if collision_with_self(snake_head, snake_position) == 1:
            crashed = True
        if collision_with_boundaries(snake_head) == 1:
            crashed = True            

        clock.tick(speed)



if __name__ == "__main__":

    # set variables

    display_width = 900

    display_height = 900

    player_color = (255,255,255)
    
    death_color = (255,100,100)

    window_color = (0,210,220)

    clock=pygame.time.Clock()



    #create the snake

    snake_head = [250,250]

    snake_position = [[250,250],[240,250],[230,250]]
    
    score = 1
    
    speed = 10


    #initialize pygame modules    

    pygame.init()



    #display game window

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Snake Game            Your score is: 0")

    pygame.display.update()



    #start the game loop

    play_game(snake_head, snake_position, 1, score, speed)



    pygame.quit()
