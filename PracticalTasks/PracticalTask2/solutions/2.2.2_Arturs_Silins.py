import turtle
t = turtle.Turtle()

def  draw_axes():
    t.color("blue")
    t.penup()
    t.goto(-300,0)
    t.pendown()
    t.goto(300,0)
    
    t.penup()
    t.goto(0,-300)
    t.pendown()
    t.goto(0,300)
    t.penup()
    
def plot_fun():
    t.color("red")
    t.goto(-250, (-250 / 5) + 7)
    t.pendown()
    for x in range(-250, 251):
        y = x / 5 + 7
        t.goto(x, y)
            
turtle.setworldcoordinates(-300, -300, 300, 300)
draw_axes()
plot_fun()
turtle.done()