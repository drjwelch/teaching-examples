# PONG pygame
# Original from https://gist.github.com/vinothpandian
#

import random
import pygame, sys
from pygame.locals import *

# Define constants

# colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

# globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
LEFT = False
RIGHT = True


class PongWindow():

    def __init__(self, *args):
        self.window = pygame.display.set_mode(*args)

    def draw(self, ball, paddles, scores):

        canvas = self.window

        # draw playing area
               
        canvas.fill(BLACK)
        pygame.draw.line(canvas, WHITE, [WIDTH // 2, 0],[WIDTH // 2, HEIGHT], 1)
        pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
        pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
        pygame.draw.circle(canvas, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)

        # draw paddles and ball
        pygame.draw.circle(canvas, RED, ball.get_pos(), BALL_RADIUS)
        for paddle in paddles:
            pygame.draw.polygon(canvas, GREEN, [[paddle.get_x() - HALF_PAD_WIDTH, paddle.get_y() - HALF_PAD_HEIGHT],
                                                [paddle.get_x() - HALF_PAD_WIDTH, paddle.get_y() + HALF_PAD_HEIGHT],
                                                [paddle.get_x() + HALF_PAD_WIDTH, paddle.get_y() + HALF_PAD_HEIGHT],
                                                [paddle.get_x() + HALF_PAD_WIDTH, paddle.get_y() - HALF_PAD_HEIGHT]], 0)

        # update scores
        font = pygame.font.SysFont("Comic Sans MS", 20)
        xpos = 50
        for score in scores:
            label = font.render("Score "+str(score), 1, (255,255,0))
            canvas.blit(label, (xpos,20))
            xpos += 420

class Paddle():

    def __init__(self, side, x, y):
        self.side = side
        self.x = x
        self.y = y
        self.speed = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_speed(self):
        return self.speed

    def set_speed(self, value):
        self.speed = value

    def move(self):
        self.y = self.y + self.speed
        
class Ball():

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        vx = random.randrange(2,4)
        vy = random.randrange(1,3)
        if direction == LEFT:
            vx = - vx
        self.speed = [vx, vy]

    def move(self):
        self.x += int(self.speed[0])
        self.y += int(self.speed[1])

    def get_pos(self):
        return (int(self.x), int(self.y))
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def bounce_y(self):
        self.bounce(1)

    def bounce_x(self):
        self.bounce(0)

    def bounce(self, axis):
        self.speed[axis] = -self.speed[axis]
        
    def speedup(self):
        self.speed[0] *= 1.1
        self.speed[1] *= 1.1
        
class PongGame():

    def __init__(self):

        # initialise pygame window (canvas)

        self.window = PongWindow((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption('Pong Game')
        pygame.init()
        self.fps = pygame.time.Clock() # assign the pygame clock to the variable fps

        border = HALF_PAD_WIDTH - 1
        self.paddles = [Paddle(LEFT, border, HEIGHT//2), Paddle(RIGHT, WIDTH - border, HEIGHT//2)]
        self.scores = [0,0]
        
        direction = random.choice([LEFT,RIGHT])
        self.ball = Ball(WIDTH//2,HEIGHT//2,direction)

    def run(self):
        
        while True:

            self.update()

            self.window.draw(self.ball, self.paddles, self.scores)

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    self.keydown(event)
                elif event.type == KEYUP:
                    self.keyup(event)
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
            
            self.fps.tick(60)
            
    # keydown handler

    def keydown(self, event):
        
        if event.key == K_UP:
            self.paddles[1].set_speed(-8)
        elif event.key == K_DOWN:
            self.paddles[1].set_speed(+8)
        elif event.key == K_w:
            self.paddles[0].set_speed(-8)
        elif event.key == K_s:
            self.paddles[0].set_speed(+8)

    # keyup handler

    def keyup(self, event):
        
        if event.key in (K_w, K_s):
            self.paddles[0].set_speed(0)
        elif event.key in (K_UP, K_DOWN):
            self.paddles[1].set_speed(0)
            
    def check_moveable(self, paddle):

        current_y = paddle.get_y()
        speed = paddle.get_speed()
        # allow paddle to move if in middle of screen ...
        if current_y > HALF_PAD_HEIGHT and current_y < HEIGHT - HALF_PAD_HEIGHT:
            return True
        # at bottom but going up
        elif current_y == HALF_PAD_HEIGHT and speed > 0:
            return True
        # at top but going down
        elif current_y == HEIGHT - HALF_PAD_HEIGHT and speed < 0:
            return True
        else:
            return False

    def update(self):
        
        # update paddle's vertical position, keep paddle on the screen

        for paddle in self.paddles:
            if self.check_moveable(paddle): paddle.move()
        
        # update ball
        self.ball.move()
        
        # ball collision check on top and bottom walls
        ypos = self.ball.get_y()
        if ypos <= BALL_RADIUS:
            self.ball.bounce_y()
        if ypos >= HEIGHT + 1 - BALL_RADIUS:
            self.ball.bounce_y()
        
        # ball collison check on gutters or paddles
        xpos = self.ball.get_x()
        threshold = BALL_RADIUS + PAD_WIDTH

        if xpos <= threshold:
            pady = self.paddles[0].get_y()
            if ypos in range(pady - HALF_PAD_HEIGHT, pady + HALF_PAD_HEIGHT):
                self.ball.bounce_x()
                self.ball.speedup()
            else:
                self.scores[1] += 1
                del self.ball
                self.ball = Ball(WIDTH//2,HEIGHT//2,RIGHT)

        if xpos >= WIDTH + 1 - threshold:
            pady = self.paddles[1].get_y()
            if ypos in range(pady - HALF_PAD_HEIGHT, pady + HALF_PAD_HEIGHT):
                self.ball.bounce_x()
                self.ball.speedup()
            else:
                self.scores[0] += 1
                del self.ball
                self.ball = Ball(WIDTH//2,HEIGHT//2,LEFT)


######################################################
#
# Main program
#
######################################################

game = PongGame()

game.run()


