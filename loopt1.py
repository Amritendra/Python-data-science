from turtle import*

#speed("fastest")

#for i in range(5):
   # forward(100)
   #10
   #  left(360/8)

#mainloop()

#pgm2
'''

sides=int(input('hpw many sidesdo u want?'))
distance=int(input('how far do u want to go?'))

for i in range(sides):
    forward(distance)
    left(360/sides)
mainloop()
'''

#pgm3
sides=6
distance=120
fillcolor("blue")
begin_fill()
for i in range(sides):
    forward(distance)
    left(360/sides)
end_fill()
mainloop()
