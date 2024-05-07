import pygame

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
display_instructions_1 = my_font.render("Player 1: WASD for movement  C to jump E to shoot", True, (235, 52, 52))
display_instructions_2 = my_font.render("Player 2: IJKL for movement  . to jump O to shoot", True, (235, 52, 52))
display_rule = my_font.render("Kill the enemy player first to win ", True, (235, 52, 52))
display_start = my_font.render("Click anywhere to start", True, (235, 52, 52))

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
        pygame.display.update()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False

pygame.quit()