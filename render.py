import pygame
import config
class Render:
    def __init__(self, screen):
        self.screen = screen
        self.green = config.COLORS["green"]
        self.white = config.COLORS["white"]
        self.black = config.COLORS["black"]
        self.red = config.COLORS["red"]
        self.background = config.COLORS["navy"]
        self.font = pygame.font.Font(None, 24)
    def draw_background(self):
        self.screen.fill(self.background)
    def draw_snake(self, snake):
        for x, y in snake.snake_body:
            pygame.draw.rect(self.screen, self.green, [x, y, config.BLOCK_SIZE, config.BLOCK_SIZE])
    def draw_food(self, food):
        x_food = food.position[0]
        y_food = food.position[1]
        pygame.draw.rect(self.screen, self.red, [x_food, y_food, config.BLOCK_SIZE, config.BLOCK_SIZE])
    def draw_score(self, score):
        text = self.font.render("Score: " + str(score), True, self.white)
        self.screen.blit(text, (10, 10))
    def draw_game_over(self):
        text = self.font.render("GAME OVER", True, self.white)
        center_x = self.screen.get_width() // 2 - text.get_width() // 2
        center_y = (self.screen.get_height() // 2) - text.get_height() // 2
        self.screen.blit(text, (center_x, center_y))

