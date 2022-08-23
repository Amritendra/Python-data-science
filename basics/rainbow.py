from turtle import*
speed(0)
colors=["red","purple",'blue',"green",'orange',"yellow"]
bgcolor("black")
pencolor("green")
for x in range(360):
    pencolor(colors[x%6])
    width(x//100+2)
    forward(x)
    left(59)
mainloop()