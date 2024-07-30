# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((320, 180))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
playerimg = pygame.image.load('Assets\images\player\player_1.png')
player = screen.blit(playerimg, player_pos)
f = pygame.Rect(0, 160, 320, 20)
rect = pygame.draw.rect(screen, "red", f)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 121, 255))

    #pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_a]:
        playerimg = pygame.image.load('Assets\images\player\player_4.png')
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        playerimg = pygame.image.load('Assets\images\player\player_1.png')
        player_pos.x += 300 * dt
    if not player.colliderect(rect):
        player_pos.y += 75 * dt
    else:
        player_pos.y = player_pos.y
    rect = pygame.draw.rect(screen, "red", f)
    screen.blit(playerimg, player_pos)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()