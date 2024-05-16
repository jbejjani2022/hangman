import pygame
import math
import sys
import random

from main import run_game


def select_word(settings):
    while True:
        rand_word = input("\nWould you like a random word? (y/n) ")
        if rand_word == 'n':
            word = input("\nEnter word (no numbers or spaces!): ")
            if " " in word or not word.isalpha():
                print("\nPlease enter valid word.")
            else:
                return word.upper()
        elif rand_word == 'y':
            print("\nRandom word generated!")
            word = random.choice(settings.WORDS)
            return word
        else:
            print("\nPlease enter y or n.")


def create_buttons(settings):
    gap = settings.GAP
    radius = settings.RADIUS
    buttons = []  # stores [x coordinate, y coordinate, letter, bool] for each button
    startx = round((settings.WIDTH - (radius * 2 + gap) * 13) / 2)
    starty = 400
    A = 65
    for i in range(26):
        x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
        y = starty + ((i // 13) * (gap + radius * 2))
        buttons.append([x, y, chr(A + i), True])
    return buttons


def draw(settings, win, word, guessed, buttons, images):
    win.fill(settings.BG_COLOR)

    draw_title(settings, win)
    draw_word(settings, win, word, guessed)
    draw_buttons(settings, win, buttons)
    # draw hangman
    win.blit(images[settings.hangman_status], (150, 100))

    pygame.display.update()


def draw_title(settings, win):
    text = settings.TITLE_FONT.render(settings.TITLE, 1, settings.TITLE_COLOR)
    win.blit(text, (settings.WIDTH / 2 - text.get_width() / 2, 20))


def draw_word(settings, win, word, guessed):
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = settings.WORD_FONT.render(display_word, 1, settings.TEXT_COLOR)
    win.blit(text, (400, 200))


def draw_buttons(settings, win, buttons):
    for button in buttons:
        x, y, letter, visible = button
        if visible:
            pygame.draw.circle(win, settings.BTN_COLOR, (x, y), settings.RADIUS, 3)
            text = settings.LETTER_FONT.render(letter, 1, settings.TEXT_COLOR)
            # draw letter in the center of button
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))


def check_events(settings, buttons, word, guessed):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            check_buttons(settings, buttons, word, guessed)


def check_buttons(settings, buttons, word, guessed):
    m_x, m_y = pygame.mouse.get_pos()
    for button in buttons:
        x, y, letter, visible = button
        if visible:
            dis = math.sqrt((m_x - x)**2 + (m_y - y)**2)
            if dis < settings.RADIUS:
                button_clicked(settings, button, letter, word, guessed)


def button_clicked(settings, button, letter, word, guessed):
    # set visible to false
    button[3] = False
    # add letter to list of guessed letters
    guessed.append(letter)
    if letter not in word and settings.hangman_status < 6:
        settings.hangman_status += 1


def check_win(settings, win, word, guessed):
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        end_game(settings, win, "You WON!")


def check_lose(settings, win):
    if settings.hangman_status == 6:
        end_game(settings, win, "You LOST!")


def end_game(settings, win, message):
    pygame.time.delay(1000)
    win.fill(settings.BG_COLOR)
    text = settings.WORD_FONT.render(message, 1, settings.END_MESSAGE_COLOR)
    win.blit(text, (settings.WIDTH / 2 - text.get_width() / 2, settings.HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(2000)
    play_again()


def play_again():
    play_again = input("\nPlay again? (y/n) ")
    if play_again == 'y':
        run_game()
    else:
        pygame.quit()
        sys.exit()
