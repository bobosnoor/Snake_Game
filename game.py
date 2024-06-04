from snake import Snake
from food import Food
from render import Render
import config
import pygame
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.width = config.WIDTH
        self.height = config.HEIGHT
        self.speed = config.SPEED
        self.block_size = config.BLOCK_SIZE
        self.score = 0
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.snake = Snake(self.block_size, self.width // 2, self.height // 2)
        self.food = Food(self.block_size, self.width, self.height, self.snake.snake_body)
        self.render = Render(self.screen)
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.render.draw_background()
            self.snake.move()
            if self.did_eat():
                self.score += 1
                self.food.position = self.food.create(self.block_size, self.width, self.height, self.snake.snake_body)
            else:
                self.snake.remove_tail()
            if self.did_collide():
                self.running = False
            self.render.draw_snake(self.snake)
            self.render.draw_food(self.food)
            self.render.draw_score(self.score)
            if not self.running:
                self.render.draw_game_over()
                pygame.display.flip()
                pygame.time.wait(2000)
            pygame.display.flip()
            self.clock.tick(self.speed)
        pygame.quit()
    def did_collide(self):
        return (
            self.snake.head[0] < 0
            or self.snake.head[0] >= self.width
            or self.snake.head[1] < 0
            or self.snake.head[1] >= self.height
            or self.snake.head  in self.snake.snake_body[1:]
        )
    def did_eat(self):
        return (
            self.snake.head[0] == self.food.position[0] 
            and self.snake.head[1] == self.food.position[1]
        )
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_key_press(event.key)
    def handle_key_press(self, key):
        if key == pygame.K_UP and self.snake.direction != "down":
            self.snake.direction = "up"
        elif key == pygame.K_DOWN and self.snake.direction != "up":
            self.snake.direction = "down"
        elif key == pygame.K_RIGHT and self.snake.direction != "left":
            self.snake.direction = "right"
        elif key == pygame.K_LEFT and self.snake.direction != "right":
            self.snake.direction = "left"

        




