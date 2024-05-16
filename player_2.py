import pygame


class Player2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["player2standing.png", "player2running.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2
        self.move = False

    def switch_image(self):
        image_number = 0
        if not self.move:
            image_number = 1
        self.image = pygame.image.load(self.image_list[image_number])
        self.image_size = self.image.get_size()
        self.move = not self.move

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
