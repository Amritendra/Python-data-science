from turtle import*

colors=["red",'blue',"pink"]
pensize(20)
for i in range(70,0,-1):
    pencolor(colors[i%3])
    forward(100)
    left(360/8)
   # circle(i*10)
    dot(i*10)


mainloop()