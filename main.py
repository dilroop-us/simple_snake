import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 600
height = 600
screen = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake settings
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

# Font
font_style = pygame.font.SysFont("sans", 25)

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 4])

def game_loop():
    game_over = False
    game_close = False

    # Snake position
    x1 = width / 2
    y1 = height / 2

    # Initial position
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:  # Handle the "game over"
            screen.fill(black)
            message("Game over! Press Q for Quit or C for Play again", red)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False  # Exit the game close loop
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False  # Exit the game close loop
                    if event.key == pygame.K_c:
                        game_close = False  # Restart the game
                        # Reset game variables
                        x1 = width / 2
                        y1 = height / 2
                        x1_change = 0
                        y1_change = 0
                        snake_list = []
                        snake_length = 1
                        food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                        food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

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
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        # Updating snake moves
        x1 += x1_change
        y1 += y1_change

        # Boundary
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Full screen
        screen.fill(black)

        # Food
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        # Snake
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Self-collision
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Drawing snake
        draw_snake(snake_block, snake_list)

        # Updating screen
        pygame.display.update()

        # Snake = food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()