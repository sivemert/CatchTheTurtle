import turtle
import time
import random

catch_the_turtle_board = turtle.Screen()
catch_the_turtle_board.bgcolor("light yellow")
catch_the_turtle_board.title("Catch the Turtle")
catch_the_turtle_board.setup(width=600, height=600)

countdown_pen = turtle.Turtle()
countdown_pen.hideturtle()
countdown_pen.penup()
countdown_pen.goto(0, 250)
countdown_pen.color("black")
countdown_pen.speed(0)

def countdown(time_sec):
    if time_sec > 0:
        countdown_pen.clear()
        countdown_pen.write("Time: " + str(time_sec), align="center", font=("Arial", 30, "normal"))
        catch_the_turtle_board.ontimer(lambda: countdown(time_sec - 1), 1000)
    else:
         countdown_pen.clear()
         countdown_pen.write("Time's Up!", align="center", font=("Arial", 30, "normal"))

countdown(20)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.setposition(-380, 250)
pen.color("black")

score = 0

target = turtle.Turtle()
target.shape("turtle")
target.color("green")
target.penup()
target.goto(0, 0)
target.hideturtle()

def update_score():
    pen.clear()
    pen.write("Score: {}".format(score), align="left", font=("Arial", 24, "normal"))

def increase_score(x, y):
    global score
    score += 10
    update_score()

def move_target():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    target.goto(x, y)
    target.showturtle()

    catch_the_turtle_board.ontimer(hide_target, 1500)

def hide_target():
    target.hideturtle()
    catch_the_turtle_board.ontimer(move_target, 1000)

target.onclick(increase_score)
update_score()
move_target()

turtle.done()
