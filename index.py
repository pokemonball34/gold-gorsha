import pygame

pygame.init()

# Display Settings
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Colour Palette
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game Caption
pygame.display.set_caption('Sample Game')

# Checks if the game should be running
is_running = True


class Block(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()


def game_loop():
    player = Block(WHITE, 200, 200)
    while is_running:
        # Event Logic Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


game_loop()

# Exits Game
pygame.quit()
quit()
