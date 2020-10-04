import turtle
purin = turtle.Turtle()
purin.color('green')
purin.shape('turtle')
canvas = turtle.Screen()
canvas.bgcolor('yellow')
#form = int(input('幾邊形'))
step = 40
purin.penup()
for i in range(300):
    purin.stamp()
    purin.forward(step)
    #angle = 360/form
    purin.left(30)
    step+=2
turtle.done()
turtle.bye()