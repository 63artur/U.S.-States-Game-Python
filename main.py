import csv
import turtle

import pandas

screen = turtle.Screen()
score = 0
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state = data['state'].to_list()
state_turtle = turtle.Turtle()
state_turtle.penup()
state_turtle.hideturtle()
guessed_states = []
missed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    elif answer_state in state:
        guessed_states.append(answer_state)
        state_input = data[data.state == answer_state]
        x,y = int(state_input['x']), int(state_input['y'])
        state_turtle.goto(x, y)
        state_turtle.write(answer_state, align="center", font=("Arial", 20, "bold"))
for guessed_state in state:
    if guessed_state not in guessed_states:
        missed_states.append(guessed_state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('learn.csv')
print(missed_states)
