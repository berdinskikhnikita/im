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
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill('black')
    pygame.mouse.set_visible(False)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                screen.fill('black')
                if pygame.mouse.get_focused():

                    pos = event.pos
                    image = load_image('arrow.png')
                    screen.blit(image, pos)



        pygame.display.flip()


    pygame.quit()
