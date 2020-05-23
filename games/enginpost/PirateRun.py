'''Classes for PirateRun game'''
import sys
import pygame


class Settings:
    '''PyrateRun game settings management class'''

    def __init__(self):
        '''Initialize settings'''

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (143, 209, 244)


class PyrateShip:
    '''PyrateShip crew'''

    def __init__(self, pr_game):
        '''shove off'''
        self.screen = pr_game.screen
        self.screen_rect = pr_game.screen.get_rect()

        # load the ship
        img = 'D:\\OneDrive\\_Projects\\_python\\samples'
        img += '\\games\\enginpost\\PyrateShip.png'
        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
        # place the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update ships position'''
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        '''draw the ship'''
        self.screen.blit(self.image, self.rect)


class PyrateRun:
    '''PyrateRun game maanger'''

    def __init__(self):
        '''Init game'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Pyrate Run')
        self.ship = PyrateShip(self)

    def run_game(self):
        '''Game loop'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    def _check_events(self):
        '''Respond to keypress and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # move the ship to the right
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
