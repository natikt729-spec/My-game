import pygame
import random

pygame.init()

# Screen
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Ultra Dodge Game")

# Player
player_x = 180
player_y = 500

# Enemies (multiple)
enemies = []
for i in range(3):
    enemies.append([random.randint(0, 350), random.randint(-600, 0)])

enemy_speed = 6

# Score
score = 0
high_score = 0
font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 60)

game_over = False

def reset_game():
    global player_x, score, enemies, game_over
    player_x = 180
    score = 0
    enemies = []
    for i in range(3):
        enemies.append([random.randint(0, 350), random.randint(-600, 0)])
    game_over = False

running = True
while running:
    screen.fill((20, 20, 20))

    # Touch control
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        player_x = x

    if not game_over:
        # Move enemies
        for enemy in enemies:
            enemy[1] += enemy_speed
            if enemy[1] > 600:
                enemy[1] = random.randint(-200, 0)
                enemy[0] = random.randint(0, 350)
                score += 1

            # Collision
            if abs(player_x - enemy[0]) < 40 and abs(player_y - enemy[1]) < 40:
                game_over = True
                if score > high_score:
                    high_score = score

    # Draw player
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 40, 40))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], 40, 40))

    # Score display
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    high_text = font.render("High: " + str(high_score), True, (255, 255, 0))
    screen.blit(high_text, (250, 10))

    # Game Over
    if game_over:
        over_text = big_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (70, 250))

        restart_text = font.render("Tap to Restart", True, (255, 255, 255))
        screen.blit(restart_text, (130, 320))

        if pygame.mouse.get_pressed()[0]:
            reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
