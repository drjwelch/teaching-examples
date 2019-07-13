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

def new_ball(direction):
    
    global ball_pos, ball_vel

    ball_pos = [WIDTH//2,HEIGHT//2]
    horz = random.randrange(2,4)
    vert = random.randrange(1,3)
    if direction == LEFT:
        horz = - horz
    ball_vel = [horz,-vert]

def move_paddle(current_y, speed):

    # allow paddle to move if in middle of screen ...
    if current_y > HALF_PAD_HEIGHT and current_y < HEIGHT - HALF_PAD_HEIGHT:
        return current_y + speed
    # at bottom but going up
    elif current_y == HALF_PAD_HEIGHT and speed > 0:
        return current_y + speed
    # at top but going down
    elif current_y == HEIGHT - HALF_PAD_HEIGHT and speed < 0:
        return current_y + speed
    else:
        return current_y

# draw function of game canvas - called to draw all objects on the screen

def draw(canvas):
    
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, l_score, r_score

    # draw playing area
           
    canvas.fill(BLACK)
    pygame.draw.line(canvas, WHITE, [WIDTH // 2, 0],[WIDTH // 2, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(canvas, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)

    # update paddle's vertical position, keep paddle on the screen

    paddle1_pos[1] = move_paddle(paddle1_pos[1], paddle1_vel)
    paddle2_pos[1] = move_paddle(paddle2_pos[1], paddle2_vel)
    
    # update ball
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])

    # draw paddles and ball
    pygame.draw.circle(canvas, RED, ball_pos, BALL_RADIUS)
    pygame.draw.polygon(canvas, GREEN, [[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT]], 0)
    pygame.draw.polygon(canvas, GREEN, [[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT]], 0)

    # ball collision check on top and bottom walls
    if int(ball_pos[1]) <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if int(ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # ball collison check on gutters or paddles
    if int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and int(ball_pos[1]) in range(paddle1_pos[1] - HALF_PAD_HEIGHT,paddle1_pos[1] + HALF_PAD_HEIGHT,1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:
        r_score += 1
        new_ball(RIGHT)
        
    if int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and int(ball_pos[1]) in range(paddle2_pos[1] - HALF_PAD_HEIGHT,paddle2_pos[1] + HALF_PAD_HEIGHT,1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
        l_score += 1
        new_ball(LEFT)

    # update scores
    font = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = font.render("Score "+str(l_score), 1, (255,255,0))
    canvas.blit(label1, (50,20))
    label2 = font.render("Score "+str(r_score), 1, (255,255,0))
    canvas.blit(label2, (470, 20))  

# keydown handler

def keydown(event):
    
    global paddle1_vel, paddle2_vel
    
    if event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 8
    elif event.key == K_w:
        paddle1_vel = -8
    elif event.key == K_s:
        paddle1_vel = 8

# keyup handler

def keyup(event):
    
    global paddle1_vel, paddle2_vel
    
    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0

######################################################
#
# Main program
#
######################################################

# initialise pygame window (canvas)

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Pong Game')
pygame.init()
fps = pygame.time.Clock() # assign the pygame clock to the variable fps

# initialise game logic

# paddles and scores
l_score = 0
r_score = 0
paddle1_pos = [HALF_PAD_WIDTH - 1,HEIGHT//2]
paddle2_pos = [WIDTH +1 - HALF_PAD_WIDTH,HEIGHT//2]
paddle1_vel = 0
paddle2_vel = 0

# create new ball to start
direction = random.choice([LEFT,RIGHT])
new_ball(direction)

# Begin game loop

while True:

    draw(window)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    
    fps.tick(60)
    
