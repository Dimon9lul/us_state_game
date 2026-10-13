import turtle
import csv

right_guesses = 0
background = turtle.Turtle()
Turtle = turtle.Turtle()
Turtle.color("black")
Turtle.hideturtle()
Turtle.penup()
screen = turtle.Screen()
screen.screensize(1, 1)
screen.title("U.S. States Game")
image = "states_map.gif"
screen.addshape(image)
background.shape(image)
with open("50_states.csv") as DATA:
    all_lists = csv.reader(DATA)
    states = []
    xs = []
    ys = []
    for v in all_lists:
        if v[0] != 'state':
            states.append(v[0])
            xs.append(v[1])
            ys.append(v[2])


def check(name):
    correct_answer = name.title()
    loop_began = True
    for i in range(0, len(states)):
        if states[i] == correct_answer:
            loop_began = False
            state = states.pop(i)
            x = xs.pop(i)
            y = ys.pop(i)
            return [True, state, x, y]
    if loop_began:
        loop_began = False
        return [False]


while True:
    answer = screen.textinput(title=f"Correct guesses {right_guesses}/50", prompt="Name a State")
    if answer is None:
        screen.exitonclick()
    else:
        returned_value = check(answer)
        if returned_value[0]:
            right_guesses += 1
            Turtle.goto(float(returned_value[2]), float(returned_value[3]))
            Turtle.write(arg=returned_value[1], move=False, align="center")
