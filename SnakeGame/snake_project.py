"""
0 . import pygame and intialize it
1. Create window where our game will be displayed and play
    -set the width and height
    -set the window game title
    -create the game loop to keep the game running until quit
2. Define the game varibales, The basic elements of our game
    - color  
    - snake size
    - game speed
    - initial score 
3. Create the snake, draw it in screen, make it move
    - snake is made of 3 blocks
4. create the food and place it randomly in the screen (but not in the snake)
5. Implement collision detection
    - snake has eaten the food (snake grows)
    - snake has hitten the window or its own body (game over)

"""
import pygame
import random
pygame.init()
clock = pygame.time.Clock()
# colors
BACKGROUND = (12,23,44)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
# block size 
block_size = 10
# game speed
speed = 10
# initial score 
score = 0

width = 640 
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
initial_x = width // 2
initial_y = height // 2
snake = [
    (initial_x, initial_y),
    (initial_x - block_size, initial_y),
    (initial_x - 2 * block_size, initial_y)
]
direction = "right"
food = None
def create_food():
    global food
    x = random.randint(0, (width - block_size) // block_size) * block_size
    y = random.randint(0, (height - block_size) // block_size) * block_size
    food = (x, y)
    while food in snake:
        x = random.randint(0, (width - block_size) // block_size) * block_size
        y = random.randint(0, (height - block_size) // block_size) * block_size
        food = (x, y)
create_food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
    screen.fill(BACKGROUND)
    #render your game here
    # move the snake
    head = snake[0] # (initial_x, initial_y)
    if direction == "up":
        new_head = (head[0], head[1] - block_size) 
    elif direction == "down":
        new_head = (head[0], head[1] + block_size)
    elif direction == "right":
        new_head = (head[0] + block_size, head[1])
    elif direction == "left":
        new_head = (head[0] - block_size, head[1])
    snake.insert(0, new_head)
    if snake[0] == food:
        score += 1
        create_food()
    else:
        snake.pop()
    if snake[0][0] < 0 or snake[0][0] >= width or snake [0][1] < 0 or snake[0][1] >= height or snake[0] in snake[1:]:
        running = False
    # draw the snake
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, [x, y, block_size, block_size])
    # draw the food
    if food is not None:
        pygame.draw.rect(screen, RED, [food[0], food[1], block_size, block_size])
    # display the score
    font = pygame.font.Font(None, 24)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))
    # check if game is over
    if not running:
        text = font.render("GAME OVER", True, WHITE)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()                                                          
