import pygame
import random
import time
from player_1 import Player1
from player_2 import Player2
from energydrink import Energydrink

pygame.init()
pygame.font.init()
pygame.mixer.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("1v1")

size = (816, 624)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("background.png")
bullet_image = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 0
bullet2_image = pygame.image.load("bullet2.png")
bullet2_x = 0
bullet2_y = 0
p1_hearts = 5
p2_hearts = 5
laser_sound = pygame.mixer.Sound("laserzap.mp3")

title_screen = True
run = True
shoot = False
shoot2 = False
game_over = False
hit = False
hit2 = False
show_energy_drink = False
current_time = time.time()
random_time = random.randint(3, 10)


display_name = my_font.render("Welcome to 1v1", True, (235, 52, 52))
display_instructions_1 = my_font.render("Player 1: WASD for movement E to shoot", True, (235, 52, 52))
display_instructions_2 = my_font.render("Player 2: IJKL for movement O to shoot", True, (235, 52, 52))
display_rule = my_font.render("Kill the enemy player first to win ", True, (235, 52, 52))
display_start = my_font.render("Click anywhere to start", True, (235, 52, 52))
display_hearts_1 = my_font.render("Player 1 Hearts: " + str(p1_hearts), True, (235, 52, 52))
display_hearts_2 = my_font.render("Player 2 Hearts: " + str(p2_hearts), True, (235, 52, 52))
display_p1_win = my_font.render("", True, (235, 52, 52))
display_p2_win = my_font.render("", True, (235, 52, 52))

p1 = Player1(255, 100)
p2 = Player2(700, 100)
eg = Energydrink(-100, -100)

counter_right1 = 0
counter_left1 = 0
counter_right2 = 0
counter_left2 = 0
direction_p1 = "right"
direction_p2 = "right"

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
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
        elapsed_time = time.time() - current_time
        time_remaining = 10 - elapsed_time
        display_hearts_1 = my_font.render("Player 1 Hearts: " + str(p1_hearts), True, (235, 52, 52))
        display_hearts_2 = my_font.render("Player 2 Hearts: " + str(p2_hearts), True, (235, 52, 52))
        clock.tick(60)
        screen.blit(bg, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            p1.move_direction("right")
            direction_p1 = "right"
            counter_right1 += 1
            if counter_right1 == 20:
                p1.switch_image()
                counter_right1 = 0
        if keys[pygame.K_a]:
            p1.move_direction("left")
            direction_p1 = "left"
            counter_left1 += 1
            if counter_left1 == 20:
                p1.switch_image()
                counter_left1 = 0
        if keys[pygame.K_w]:
            p1.move_direction("up")
        if keys[pygame.K_s]:
            p1.move_direction("down")
        if keys[pygame.K_l]:
            p2.move_direction("right")
            direction_p2 = "right"
            counter_right2 += 1
            if counter_right2 == 20:
                p2.switch_image()
                counter_right2 = 0
        if keys[pygame.K_j]:
            p2.move_direction("left")
            direction_p2 = "left"
            counter_left2 += 1
            if counter_left2 == 20:
                p2.switch_image()
                counter_left2 = 0
        if keys[pygame.K_i]:
            p2.move_direction("up")
        if keys[pygame.K_k]:
            p2.move_direction("down")
        if keys[pygame.K_e] and not shoot:
            laser_sound.play()
            initial_bullet_x = p1.rect.centerx
            initial_bullet_y = p1.rect.centery
            bullet_x = initial_bullet_x
            bullet_y = initial_bullet_y
            direction = direction_p1
            shoot = True
        if keys[pygame.K_o] and not shoot2:
            laser_sound.play()
            initial_bullet2_x = p2.rect.centerx
            initial_bullet2_y = p2.rect.centery
            bullet2_x = initial_bullet2_x
            bullet2_y = initial_bullet2_y
            direction2 = direction_p2
            shoot2 = True
        if p2.rect.collidepoint(bullet_x, bullet_y) and not hit2:
            hit2 = True
            p2_hearts -= 1
            display_hearts_2 = my_font.render("Player 2 Hearts: " + str(p2_hearts), True, (235, 52, 52))
        if p1.rect.collidepoint(bullet2_x, bullet2_y) and not hit:
            hit = True
            p1_hearts -= 1
            display_hearts_1 = my_font.render("Player 1 Hearts: " + str(p1_hearts), True, (235, 52, 52))
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                run = False
        if shoot:
            screen.blit(bullet_image, (bullet_x, bullet_y))
            if direction == "right":
                bullet_x += 10
            else:
                bullet_x -= 10
            if bullet_x > 1072 or bullet_x < 0:
                shoot = False
                hit2 = False
        if shoot2:
            screen.blit(bullet2_image, (bullet2_x, bullet2_y))
            if direction2 == "right":
                bullet2_x += 10
            else:
                bullet2_x -= 10
            if bullet2_x > 816 or bullet2_x < 0:
                shoot2 = False
                hit = False
        if time_remaining <= random_time and not show_energy_drink:
            show_energy_drink = True
            eg.set_location(random.randint(40, 800), random.randint(40, 400))
            energy_drink_timer = time.time()
        if show_energy_drink:
            if p1.rect.colliderect(eg.rect):
                p1_hearts += 2
                eg = Energydrink(-100, -100)
            if p2.rect.colliderect(eg.rect):
                p2_hearts += 2
                eg = Energydrink(-100, -100)
        if p1_hearts <= 0 or p2_hearts <= 0:
            display_p2_win = my_font.render("Player 2 Wins!", True, (235, 52, 52))
            display_p1_win = my_font.render("Player 1 Wins!", True, (235, 52, 52))
            game_over = True
        if game_over:
            if p1_hearts <= 0:
                screen.blit(display_p2_win, (500, 200))
            if p2_hearts <= 0:
                screen.blit(display_p1_win, (500, 200))
        else:
            if show_energy_drink:
                screen.blit(eg.image, eg.rect)
            screen.blit(display_hearts_1, (0, 0))
            screen.blit(display_hearts_2, (0, 15))
            screen.blit(p1.image, p1.rect)
            screen.blit(p2.image, p2.rect)
        pygame.display.update()
        frame += 1

pygame.quit()
