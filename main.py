import pygame
from player_1 import Player1
from player_2 import Player2

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("1v1")

size = (1072, 600)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("background.png")

title_screen = True
run = True

display_name = my_font.render("Welcome to 1v1", True, (235, 52, 52))
display_instructions_1 = my_font.render("Player 1: WASD for movement E to shoot", True, (235, 52, 52))
display_instructions_2 = my_font.render("Player 2: IJKL for movement O to shoot", True, (235, 52, 52))
display_rule = my_font.render("Kill the enemy player first to win ", True, (235, 52, 52))
display_start = my_font.render("Click anywhere to start", True, (235, 52, 52))

p1 = Player1(255, 100)
p2 = Player2(700, 100)
counter = 0
counter2 = 0

# -------- Main Program Loop -----------
frame = 0
while run:
    # --- Main event loop
    if title_screen:
        screen.blit(bg, (0, 0))
        screen.blit(display_name, (330, 200))
        screen.blit(display_instructions_1, (330, 230))
        screen.blit(display_instructions_2, (330, 250))
        screen.blit(display_rule, (330, 270))
        screen.blit(display_start, (330, 290))
        pygame.display.update()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                title_screen = False
    else:
        screen.blit(bg, (0, 0))
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            p1.move_direction("right")
            counter = counter + 1
            if counter == 20:
                p1.switch_image()
                counter = 0
        if keys[pygame.K_a]:
            p1.move_direction("left")
            counter = counter + 1
            if counter == 20:
                p1.switch_image()
                counter = 0
        if keys[pygame.K_w]:
            p1.move_direction("up")
        if keys[pygame.K_s]:
            p1.move_direction("down")
        if keys[pygame.K_l]:
            p2.move_direction("right")
            counter2 = counter2 + 1
            if counter2 == 20:
                p2.switch_image()
                counter2 = 0
        if keys[pygame.K_j]:
            p2.move_direction("left")
            counter2 = counter2 + 1
            if counter2 == 20:
                p2.switch_image()
                counter2 = 0
        if keys[pygame.K_i]:
            p2.move_direction("up")
        if keys[pygame.K_k]:
            p2.move_direction("down")
        pygame.display.update()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False

pygame.quit()