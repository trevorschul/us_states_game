import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

turtle.shape(image)
data = pandas.read_csv("50_states.csv")

game_is_on = True
score = 0
correct_guesses = []
missing_states = []
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State {score}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [s for s in data["state"] if s not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_study.csv")
        game_is_on = False
    for state in data["state"]:
        if answer_state == state and state not in correct_guesses:
            score += 1
            correct_guesses.append(state)
            print(correct_guesses)
            state_holder = data[data.state == state]
            x_coor = int(state_holder.x)
            y_coor = int(state_holder.y)
            writer.setposition(x_coor, y_coor)
            writer.write(state)
    if score == 50:
        game_is_on = False



screen.exitonclick()