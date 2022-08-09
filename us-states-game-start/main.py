from turtle import Turtle, Screen
import turtle
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
user_guesses = []
list_of_states = data["state"].to_list()


while len(user_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(user_guesses)}/50", prompt="Guess a state").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in list_of_states if state not in user_guesses]

    #     states_to_learn = []
    #     for state in list_of_states:
    #         if state not in user_guesses:
    #             states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in list_of_states:
        user_guesses.append(answer_state)
        t = Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# states_to_learn.csv
#save states not guessed to the csv



turtle.mainloop()