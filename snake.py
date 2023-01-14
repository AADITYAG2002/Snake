import pygame as pg

class Game:
    def __init__(self, width, height) :
        pg.init()
        self.screen = pg.display.set_mode((width,height))
        self.clock = pg.time.Clock()

        snake = Snake_Head(self,100,100,10,0)
        snake_body = []
        snake_body.append(Snake_Body(self,snake.x-10,snake.y))
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
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    snake_body.append(Snake_Body(self,snake_body[len(snake_body)-1].x-snake.vel_x,snake_body[len(snake_body)-1].y-snake.vel_y))


            for i in range(len(snake_body)-1,-1,-1):
                if i == 0:
                    snake_body[0].update(snake.x, snake.y)
                else:
                    snake_body[i].update(snake_body[i-1].x, snake_body[i-1].y)
            snake.update()

            pg.display.flip()
            self.clock.tick(10)
            self.screen.fill((0,0,0))

            snake.checkCollision(self)

            snake.draw()
            for part in snake_body:
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
        self.x += self.vel_x
        self.y += self.vel_y

class Snake_Body:
    def __init__(self,game,x,y):
        self.x = x
        self.y = y
        self.size = 10
        self.game = game
    
    def draw(self):
        pg.draw.rect(self.game.screen,(0,255,0),pg.Rect(self.x,self.y,self.size,self.size))
    
    def update(self,x,y):
        self.x = x
        self.y = y


class Apple:
    def __init__(self,game,x,y):
        self.x = x
        self.y = y
        self.game = game
        pg.draw.rect(self.game.screen,(255,0,0),pg.Rect(x,y,10,10))

if __name__ == '__main__':
    game = Game(720,480)