import pygame


class Settings():
    def __init__(self):
        # display variables
        self.WIDTH, self.HEIGHT = 800, 500
        self.CAPTION = "Hangman"
        self.FPS = 60

        self.TITLE = "DEVELOPER HANGMAN"

        # fonts
        self.LETTER_FONT = pygame.font.SysFont('comicsans', 40)
        self.WORD_FONT = pygame.font.SysFont('comicsans', 60)
        self.TITLE_FONT = pygame.font.SysFont('comicsans', 70)

        # colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.ORANGE = (255, 140, 0)
        self.BG_COLOR = self.WHITE
        self.TEXT_COLOR = self.BLACK
        self.BTN_COLOR = self.BLACK  # button color
        self.END_MESSAGE_COLOR = self.ORANGE
        self.TITLE_COLOR = self.ORANGE

        # button variables
        self.RADIUS = 20
        self.GAP = 15

        # TRY IMPLEMENTING WORDS WITH SPACES
        self.WORDS = ["PYTHON", "PYGAME", "DEVELOPER", "COMPSCI", "CODE"]

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.hangman_status = 0
