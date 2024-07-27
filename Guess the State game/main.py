import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. states Game")
image="img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
guessed_states=[]
count=0
for i in range(1,51):
    answer_state=screen.textinput(title=f"{count}/50 State correct", prompt="What's another state's name?").title()
    if answer_state=="Exit":
        break
    if answer_state in data.state.to_list() and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]
        guessed_states.append(state_data.state.item())
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        
        # Create a turtle to write the state name
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(x_cor, y_cor)
        pen.write(state_data.state.item())
        
        count += 1
sl={"State":[]}
for i in data.state.to_list():
    if i not in guessed_states:
        sl["State"].append(i)
pandas.DataFrame(sl).to_csv("State to be learned")