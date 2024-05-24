import turtle as t
import os
import random

# スコアの初期値を設定
score_A = 0
score_B = 0

# ゲーム画面を生成
window = t.Screen()
window.title("PingPong Game")
window.bgcolor("blue")
window.setup(width=800, height=600)
window.tracer(0)

# 左のバー作成
left_bar = t.Turtle()
left_bar.speed(0)
left_bar.shape("square")
left_bar.color("white")
left_bar.shapesize(stretch_len=1, stretch_wid=5)
left_bar.penup()
left_bar.goto(-350, 0)

# 右のバー作成
right_bar = t.Turtle()
right_bar.speed(0)
right_bar.shape("square")
right_bar.color("white")
right_bar.shapesize(stretch_len=1, stretch_wid=5)
right_bar.penup()
right_bar.goto(350, 0)

# ボールの作成
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball_x_direction = random.uniform(-0.5, 0.5)
if ball_x_direction <= -0.25 or ball_x_direction <= 0.25:
    ball_x_direction = random.uniform(-0.5, 0.5)
ball_y_direction = random.uniform(-0.75, 0.75)
if ball_y_direction <= -0.25 or ball_y_direction <= 0.25:
    ball_y_direction = random.uniform(-0.75, 0.75)

# スコアボード
score_board = t.Turtle()
score_board.speed(0)
score_board.color("yellow")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("PlayerA: 0         PlayerB: 0", align="center", font=('Arial', 24, 'normal'))


# バーの上下
def left_bar_up():
    y = left_bar.ycor()
    y = y + 20
    left_bar.sety(y)


def left_bar_down():
    y = left_bar.ycor()
    y = y - 20
    left_bar.sety(y)


def right_bar_up():
    y = right_bar.ycor()
    y = y + 20
    right_bar.sety(y)


def right_bar_down():
    y = right_bar.ycor()
    y = y - 20
    right_bar.sety(y)


window.listen()
window.onkeypress(left_bar_up, 'w')
window.onkeypress(left_bar_down, 's')
window.onkeypress(right_bar_up, 'Up')
window.onkeypress(right_bar_down, 'Down')

while True:
    # 画面を更新する
    window.update()
    # ボールを動かす
    ball.setx(ball.xcor() + ball_x_direction)
    ball.sety(ball.ycor() + ball_y_direction)

    # ボールが壁に当たったとき
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y_direction = ball_y_direction * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_y_direction = ball_y_direction * -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_A = score_A + 1
        score_board.clear()
        score_board.write("player A:{}       player B:{}".format(score_A, score_B), align='center',
                          font=('Arial', 24, 'normal'))
        ball_x_direction = random.uniform(-0.5, 0.5)
        if ball_x_direction <= -0.25 or ball_x_direction <= 0.25:
            ball_x_direction = random.uniform(-0.5, 0.5)
        ball_y_direction = random.uniform(-0.75, 0.75)
        if ball_y_direction <= -0.25 or ball_y_direction <= 0.25:
            ball_y_direction = random.uniform(-0.75, 0.75)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        score_B = score_B + 1
        score_board.clear()
        score_board.write("player A:{}       player B:{}".format(score_A, score_B), align='center',
                          font=('Arial', 24, 'normal'))
        ball_x_direction = random.uniform(-0.5, 0.5)
        if ball_x_direction <= -0.25 or ball_x_direction <= 0.25:
            ball_x_direction = random.uniform(-0.5, 0.5)
        ball_y_direction = random.uniform(-0.75, 0.75)
        if ball_y_direction <= -0.25 or ball_y_direction <= 0.25:
            ball_y_direction = random.uniform(-0.75, 0.75)
        
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            ball.ycor() < right_bar.ycor() + 40 and ball.ycor() > right_bar.ycor() - 40):
        ball.setx(340)
        ball_x_direction = ball_x_direction * -1
        if ball_x_direction >= 0:
            ball_x_direction = ball_x_direction + 0.05
        else:
            ball_x_direction = ball_x_direction - 0.05

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            ball.ycor() < left_bar.ycor() + 40 and ball.ycor() > left_bar.ycor() - 40):
        ball.setx(-340)
        ball_x_direction = ball_x_direction * -1
        if ball_x_direction >= 0:
            ball_x_direction = ball_x_direction + 0.05
        else:
            ball_x_direction = ball_x_direction - 0.05