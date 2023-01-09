from turtle import Turtle, Screen
import pandas

screen = Screen()
tom = Turtle()
img="blank_states_img.gif"
screen.addshape(img)
screen.title("USA-guessing state game")

tom.shape(img)
correct = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{correct}/50 Correct State", prompt="type USA states name:").title()
    if answer_state=="Exit":
        missing_state=[]
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # item() is method of pandas series to return first element only
        # or you can write t.write(state_answer)
        t.write(state_data.state.item())
        correct += 1

