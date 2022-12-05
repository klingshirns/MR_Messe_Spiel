import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('=', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.charactersx, self.charactersy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Hauptmenü', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start", 20, self.startx, self.starty)
            self.game.draw_text("Kultur-Vorbilder", 20, self.charactersx, self.charactersy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.charactersx + self.offset, self.charactersy)
                self.state = 'Kultur-Vorbilder'
            elif self.state == 'Kultur-Vorbilder':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Kultur-Vorbilder':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.charactersx + self.offset, self.charactersy)
                self.state = 'Kultur-Vorbilder'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Kultur-Vorbilder':
                self.game.curr_menu = self.game.characters
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class CharacterMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Einfachmacher'
        self.character1x, self.character1y = self.mid_w, self.mid_h + 20
        self.character2x, self.character2y = self.mid_w, self.mid_h + 40
        self.character3x, self.character3y = self.mid_w, self.mid_h + 60
        self.character4x, self.character4y = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.character1x + self.offset, self.character1y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Kultur-Vorbilder', 35, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Einfachmacher", 20, self.character1x, self.character1y)
            self.game.draw_text("Zusammenbringer", 20, self.character2x, self.character2y)
            self.game.draw_text("Vorangeher", 20, self.character3x, self.character3y)
            self.game.draw_text("Kundenversteher", 20, self.character4x, self.character4y)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.DOWN_KEY:
            if self.state == 'Einfachmacher':
                self.state = 'Zusammenbringer'
                self.cursor_rect.midtop = (self.character2x + self.offset, self.character2y)
            elif self.state == 'Zusammenbringer':
                self.state = 'Vorangeher'
                self.cursor_rect.midtop = (self.character3x + self.offset, self.character3y)
            elif self.state == 'Vorangeher':
                self.state = 'Kundenversteher'
                self.cursor_rect.midtop = (self.character4x + self.offset, self.character4y)
            elif self.state == 'Kundenversteher':
                self.state = 'Einfachmacher'
                self.cursor_rect.midtop = (self.character1x + self.offset, self.character1y)
        elif self.game.UP_KEY:
            if self.state == 'Einfachmacher':
                self.state = 'Kudenversteher'
                self.cursor_rect.midtop = (self.character4x + self.offset, self.character4y)
            elif self.state == 'Kundenversteher':
                self.state = 'Vorangeher'
                self.cursor_rect.midtop = (self.character3x + self.offset, self.character3y)
            elif self.state == 'Vorangeher':
                self.state = 'Zusammenbringer'
                self.cursor_rect.midtop = (self.character2x + self.offset, self.character2y)
            elif self.state == 'Zusammenbringer':
                self.state = 'Einfachmacher'
                self.cursor_rect.midtop = (self.character1x + self.offset, self.character1y)
        elif self.game.START_KEY:
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 35, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by MR IT-Azubis 2021', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()