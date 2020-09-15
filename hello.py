import turtle
q=turtle.Pen()
turtle.bgcolor("black")
sides = 6
colors =["purple","blue","green","yellow","orange","red"]
for x in range(360):
    q.pencolor(colors[x%sides])
    q.forward(x*3/sides+1)
    q.left(360/sides+1)
    q.width(x*sides/500)
