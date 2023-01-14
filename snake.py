import pygame as pg
import random as rd

class Game:
    snake_body = []
    def __init__(self, width, height) :
        self.width = width
        self.height = height
        pg.init()
        self.screen = pg.display.set_mode((width,height))
        self.clock = pg.time.Clock()

        snake = Snake_Head(self,100,100,10,0)
        apple = Apple(self,rd.randrange(0,width,10),rd.randrange(0,height,10),snake)
        
        self.snake_body.append(Snake_Body(self,snake.x-10,snake.y))
        while True:
            pressed = pg.key.get_pressed()
            if pressed[pg.K_UP]:
                snake.vel_x, snake.vel_y = 0, -10
            elif pressed[pg.K_LEFT]:
                snake.vel_x, snake.vel_y = -10, 0
            elif pressed[pg.K_RIGHT]:
                snake.vel_x, snake.vel_y = 10, 0
            elif pressed[pg.K_DOWN]:
                snake.vel_x, snake.vel_y = 0, 10

            for event in pg.event.get():
                if event.type == pg.QUIT: 
                    quit()
                # if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    


            for i in range(len(self.snake_body)-1,-1,-1):
                if i == 0:
                    self.snake_body[0].update(snake.x, snake.y)
                else:
                    self.snake_body[i].update(self.snake_body[i-1].x, self.snake_body[i-1].y)
            snake.update()

            pg.display.flip()
            self.clock.tick(10)
            self.screen.fill((0,0,0))

            snake.checkCollision(self)
            apple.checkCollision(self)
            
            snake.draw()
            apple.draw()
            for part in self.snake_body:
                part.draw()
                
class Snake_Head:
    def __init__(self,game,x,y,vel_x,vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.game = game
        self.size = 10
    
    def draw(self):
        pg.draw.rect(self.game.screen,(0,255,0),pg.Rect(self.x,self.y,self.size,self.size))
    
    def checkCollision(self,game):
        for part in game.snake_body:
            if (part.x < self.x + self.size and
                    part.x > self.x - self.size and
                    part.y < self.y + self.size and
                    part.y > self.y - self.size):
                quit()

    def update(self):
        if self.x > self.game.width:
            self.x = 0
        elif self.x < 0:
            self.x = self.game.width
        else:
            self.x += self.vel_x
        if self.y > self.game.height:
            self.y = 0
        elif self.y < 0:
            self.y = self.game.height
        else:
            self.y += self.vel_y

class Apple(Snake_Head):
    def __init__(self,game,x,y,snake):
        self.snake = snake
        self.x = x
        self.y = y
        self.game = game
    
    def draw(self):
        pg.draw.rect(self.game.screen,(255,0,0),pg.Rect(self.x,self.y,10,10))
    
    def checkCollision(self,game):
        if (self.snake.x < self.x + self.snake.size and
                self.snake.x > self.x - self.snake.size and
                self.snake.y < self.y + self.snake.size and
                self.snake.y > self.y - self.snake.size):
            
            game.snake_body.append(Snake_Body(game,game.snake_body[len(game.snake_body)-1].x-self.snake.vel_x,game.snake_body[len(game.snake_body)-1].y-self.snake.vel_y))
            self.x = rd.randrange(0,game.width,10)
            self.y = rd.randrange(0,game.height,10)

class Snake_Body:
    def __init__(self,game,x,y):
        self.x = x
        self.y = y
        self.size = 10
        self.game = game
    
    def draw(self):
        pg.draw.rect(self.game.screen,(0,200,0),pg.Rect(self.x,self.y,self.size,self.size))
    
    def update(self,x,y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    game = Game(720,480)