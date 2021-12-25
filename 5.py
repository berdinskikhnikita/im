import pygame
import os
import sys

SIZE = WIDTH, HEIGHT = 600, 300


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill('blue')
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image('gameover.png')
    sprite.rect = sprite.image.get_rect()
    clock = pygame.time.Clock()
    fps = 60
    v = 200
    sprite.rect.x, sprite.rect.y = -600, 0
    all_sprites = pygame.sprite.Group()
    all_sprites.add(sprite)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if sprite.rect.x < 0:
            sprite.rect.x += v / fps
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
