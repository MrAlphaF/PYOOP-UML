import turtle
t = turtle.Turtle()

def draw_star(n, lenght):

    angle = 180-(180/n)
    for _ in range(n):
        t.speed(0)
        t.forward(lenght)  
        t.right(angle)    

    turtle.done()
    
draw_star(101,400)