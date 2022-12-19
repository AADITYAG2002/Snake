import pygame as pg

class Game:
    def __init__(self, width, height) :
        pg.init()
        self.screen = pg.display.set_mode((width,height))

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT: quit()
                pg.display.flip()
                self.screen.fill((0,0,0))

if __name__ == '__main__':
    game = Game(720,480)