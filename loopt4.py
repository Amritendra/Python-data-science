from turtle import*
speed(0)
pencolor("white")
bgcolor('black')
pensize(2)
for i in range(20):
    penup()
    forward(150)
    pendown()
    left(360/8)
    dot(10,("red"))
    circle(100,50)
    for i in range(7):
        forward(-70)
        left(360/8)
        circle(50,20)
        dot(15,('blue'))
hideturtle()

mainloop()
