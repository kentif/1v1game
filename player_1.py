import pygame


class Player1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["player1standing.png", "player1running.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.image2 = pygame.image.load(self.image_list[1])
        self.images = [self.image, self.image2]
        self.flipped_image = pygame.transform.flip(self.image, True, False)
        self.flipped_image2 = pygame.transform.flip(self.image2, True, False)
        self.flipped_images = [self.flipped_image, self.flipped_image2]
        self.image = self.images[0]
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2
        self.move = False
        self.current_direction = "right"

    def move_direction(self, direction):
        if direction == "right" and self.current_direction == "left":
            self.current_direction = "right"
        if direction == "left" and self.current_direction == "right":
            self.current_direction = "left"
        if direction == "right":
            self.x += self.delta
        if direction == "left":
            self.x -= self.delta
        if direction == "down":
            self.y += self.delta
        if direction == "up":
            self.y -= self.delta

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def switch_image(self):
        if self.move:
            if self.current_direction == "right":
                self.image = self.images[1]
            else:
                self.image = self.flipped_images[1]
        else:
            if self.current_direction == "right":
                self.image = self.images[0]
            else:
                self.image = self.flipped_images[0]

        self.image_size = self.image.get_size()
        self.move = not self.move


