from turtle import*
speed(0)
pencolor('green')
bgcolor('orange')
val=1
while True:
    forward(3*val)
    left(360/6)
    circle(10,val)
    dot(10,"white")
    val+=1

