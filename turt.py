import turtle


scree = turtle.Screen()
turt = turtle.Turtle()
turt.speed(100)
bruh = 1
colors = ["red", "blue", "green", "purple"]
color = 0
color2 = 1
def drawSpiral(myTurtle, linelen):
    turt.forward(linelen)
    turt.right(90)
    drawSpiral(turt, linelen-10)
for i in range(500):
    turt.forward(bruh)
    turt.right(bruh)
    bruh += 1
    #turt.color(colors[color])
    turt.color((color2,41,255 - color2))
    color2 += 1
    if color2 == 255:
        color2 = 1

drawSpiral(turt, 80)
scree.exitonclick()