import pygame
from player_1 import Player_1

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("1v1")

size = (1138, 600)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("background.png")

title_screen = True
run = True

display_name = my_font.render("Welcome to 1v1", True, (235, 52, 52))
display_instructions_1 = my_font.render("Player 1: AD for movement  W to jump E to shoot", True, (235, 52, 52))
display_instructions_2 = my_font.render("Player 2: JL for movement  I to jump O to shoot", True, (235, 52, 52))
display_rule = my_font.render("Kill the enemy player first to win ", True, (235, 52, 52))
display_start = my_font.render("Click anywhere to start", True, (235, 52, 52))

p1 = Player_1(200, 200)

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
        screen.blit(p1.image, (200, 200))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            p1.move_direction("right")
            p1.switch_image()
        if keys[pygame.K_a]:
            p1.move_direction("left")
            p1.switch_image()
        if keys[pygame.K_w]:
            p1.move_direction("up")
        if keys[pygame.K_s]:
            p1.move_direction("down")

        pygame.display.update()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False

pygame.quit()