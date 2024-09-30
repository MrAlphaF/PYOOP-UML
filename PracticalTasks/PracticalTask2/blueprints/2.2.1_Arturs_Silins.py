import turtle
t = turtle.Turtle()

n=11
angle = 180-(180/n)
for _ in range(n):
    t.forward(300)  
    t.right(angle)    


turtle.done()