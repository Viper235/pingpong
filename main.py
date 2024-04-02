import pygame as pg
from setings import *


class Game():

    def __init__(self):
        #Запускаем движок Pygame
        pg.init()
        self.window = pg.display.set_mode((W_WIDTH, W_HIGHT))
        self.new_game()

    def new_game(self):
        '''
        Метод отвечает за запуск новой игры
        '''
        #Переменная игрового цикла
        self.run_game = True
        self.clock = pg.time.Clock()
        self.bg = pg.transform.scale(pg.image.load('bg.jpg'), (W_WIDTH, W_HIGHT))


    def update(self):
        '''
        Меняем положение спрайтов
        '''
        pg.display.update()
        
    def draw(self):
        '''
        Отрисовываем спрайты в окне
        '''
        self.window.blit(self.bg, (0,0))
     


    def run(self):
        '''
        Запуск игрового цикла 
        '''
        while self.run_game:
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
    