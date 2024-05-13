import pygame
import time

class Player1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["player1standing.png", "player1running.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3
        self.move = False

    def switch_image(self):
        image_number = 0
        current_time = time.time()
        elapsed_time = time.time() - current_time
        if elapsed_time > 1:
            image_number = 1
            elapsed_time = 0
        self.image = pygame.image.load(self.image_list[image_number])
        self.image_size = self.image.get_size()

    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "left":
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up":
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
