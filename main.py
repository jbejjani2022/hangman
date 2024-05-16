import pygame

from settings import Settings
import game_functions as gf


def run_game():
    pygame.init()
    settings = Settings()
    # win stands for window
    win = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption(settings.CAPTION)
    clock = pygame.time.Clock()

    # load images
    images = []
    for i in range(7):
        image = pygame.image.load("images/hangman{}.png".format(str(i)))
        images.append(image)

    # game variables
    buttons = gf.create_buttons(settings)
    word = gf.select_word(settings)
    guessed = []

    # main game loop
    while True:
        clock.tick(settings.FPS)
        gf.check_events(settings, buttons, word, guessed)
        gf.draw(settings, win, word, guessed, buttons, images)
        gf.check_win(settings, win, word, guessed)
        gf.check_lose(settings, win)


if __name__ == "__main__":
    run_game()
