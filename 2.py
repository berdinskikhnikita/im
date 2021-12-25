import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill('white')
    x, y = 0, 0
    image = load_image('creature.png')
    screen.blit(image, (x, y))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    screen.fill('white')
                    y -= 10
                    load_image('creature.png')
                    screen.blit(image, (x, y))
                if event.key == pygame.K_DOWN:
                    screen.fill('white')
                    y += 10
                    load_image('creature.png')
                    screen.blit(image, (x, y))
                if event.key == pygame.K_RIGHT:
                    screen.fill('white')
                    x += 10
                    load_image('creature.png')
                    screen.blit(image, (x, y))
                if event.key == pygame.K_LEFT:
                    screen.fill('white')
                    x -= 10
                    load_image('creature.png')
                    screen.blit(image, (x, y))

        pygame.display.flip()

    pygame.quit()
