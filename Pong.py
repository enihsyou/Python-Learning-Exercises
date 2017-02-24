# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 8
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = WIDTH / 2
HALF_PAD_HEIGHT = HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [HALF_PAD_WIDTH, HALF_PAD_HEIGHT]
ball_vel = [0, 0]
paddle1_pos = [0, (HEIGHT - PAD_HEIGHT) // 2]
paddle2_pos = [WIDTH - PAD_WIDTH, (HEIGHT - PAD_HEIGHT) // 2]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
speed = 1
added = False

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left


def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [HALF_PAD_WIDTH, HALF_PAD_HEIGHT]
    if direction == RIGHT:
        ball_vel = [random.randrange(2, 4), -random.randrange(1, 3)]
        # ball_vel = [2, -2]
    else:
        ball_vel = [-random.randrange(2, 4), -random.randrange(1, 3)]
        # ball_vel = [-2, -2]


def postionchanger(paddlepos):  # return a list of needed positions
    upper1 = paddlepos
    upper2 = [paddlepos[0] + PAD_WIDTH, paddlepos[1]]
    down1 = [paddlepos[0], paddlepos[1] + PAD_HEIGHT]
    down2 = [paddlepos[0] + PAD_WIDTH, paddlepos[1] + PAD_HEIGHT]
    return [upper1, upper2, down2, down1]


def restart():  # restart a game depend on the last result
    if ball_pos[0] < HALF_PAD_WIDTH:
        spawn_ball(RIGHT)
    if ball_pos[0] > HALF_PAD_WIDTH:
        spawn_ball(LEFT)
    global added, speed
    added = False
    speed = 1
# define event handlers


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)
    paddle1_pos = [0, (HEIGHT - PAD_HEIGHT) // 2]
    paddle2_pos = [WIDTH - PAD_WIDTH, (HEIGHT - PAD_HEIGHT) // 2]
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0 


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, speed
    global added

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0] * speed
    ball_pos[1] += ball_vel[1] * speed
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = [paddle1_pos[0], paddle1_pos[1] + paddle1_vel]
    paddle2_pos = [paddle2_pos[0], paddle2_pos[1] + paddle2_vel]

    if paddle1_pos[1] <= 0:
        paddle1_pos[1] = 0
    elif paddle1_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT
    if paddle2_pos[1] <= 0:
        paddle2_pos[1] = 0
    elif paddle2_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - PAD_HEIGHT
    # draw paddles
    canvas.draw_polygon(postionchanger(paddle1_pos), 1, 'White', 'White')
    canvas.draw_polygon(postionchanger(paddle2_pos), 1, 'White', 'White')
    # determine whether paddle and ball collide

    # paddle and ball collide
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:  # left
        if ball_pos[1] < paddle1_pos[1] + PAD_HEIGHT and ball_pos[1] > paddle1_pos[1]:
            ball_vel[0] = -ball_vel[0]
            speed += 0.1
        else:
            if not added:
                score2 += 1
                added = True

    if WIDTH - PAD_WIDTH - ball_pos[0] <= BALL_RADIUS:  # right
        if ball_pos[1] < paddle2_pos[1] + PAD_HEIGHT and ball_pos[1] > paddle2_pos[1]:
            ball_vel[0] = -ball_vel[0]
            speed += 0.1
        else:
            if not added:
                score1 += 1
                added = True

    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] + BALL_RADIUS >= WIDTH:
        restart()

    # vertical
    if ball_pos[1] <= BALL_RADIUS or HEIGHT - ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # draw scores
    canvas.draw_text(str(score1), (100, 100), 30, 'White')
    canvas.draw_text(str(score2), (400, 100), 30, 'White')


def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 6
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 6
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 6
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 6


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel += 6
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel -= 6
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += 6
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel -= 6

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('RESTART', new_game)

# start frame
new_game()
frame.start()
