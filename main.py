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
# -------- Main Program Loop -----------
frame = 0
while run:
    # --- Main event loop
    if title_screen:
        screen.blit(bg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                title_screen = False
    else:
        screen.blit(bg, (0, 0))

pygame.quit()