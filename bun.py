import pygame
import os

pygame.init()
background = (24, 113, 147)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 300
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Bun')

bun = pygame.image.load("my_pictures/bun.png")

bun_angle = 0
bun_rotation_speed = 2

fox = []
for i in range(8):
    fox_surface = pygame.Surface((80, 60), pygame.SRCALPHA)
    color = (255, 100, 0) if i < 4 else (255, 120, 0)
    pygame.draw.ellipse(fox_surface, color, (0, 10, 60, 40))
    pygame.draw.polygon(fox_surface, color, [(60, 20), (80, 10), (80, 40)])
    pygame.draw.circle(fox_surface, (0, 0, 0), (15, 25), 5)
    pygame.draw.circle(fox_surface, (0, 0, 0), (35, 25), 5)
    fox.append(fox_surface)

fox_frame = 0
fox_frame_rate = 8
fox_frame_timer = 0

bun_x = 100
bun_y = 150
fox_x = 0
fox_y = 150
movement_speed = 3

clock = pygame.time.Clock()

game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    bun_angle = (bun_angle + bun_rotation_speed) % 360
    rotated_bun = pygame.transform.rotate(bun, bun_angle)
    bun_rect = rotated_bun.get_rect(center=(bun_x + bun.get_width()//2, bun_y + bun.get_height()//2))

    bun_x += movement_speed
    fox_x += movement_speed + 1

    if bun_x > WINDOW_WIDTH:
        bun_x = -bun.get_width()
    if fox_x > WINDOW_WIDTH:
        fox_x = -80

    fox_frame_timer += clock.tick(60)
    if fox_frame_timer >= 1000 / fox_frame_rate:
        fox_frame_timer -= 1000 / fox_frame_rate
        fox_frame = (fox_frame + 1) % len(fox)

    game_display.fill(background)
    game_display.blit(rotated_bun, bun_rect)
    game_display.blit(fox[fox_frame], (fox_x, fox_y))
    pygame.display.update()

pygame.quit()
