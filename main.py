#import
import random
import emojis
import time
import turtle
#import antigravity
#defs
# Turtle to draw a spiral
def drawSpiral(myTurtle, linelen):
    turt.forward(linelen)
    turt.right(90)
    drawSpiral(turt, linelen-10)
alltilr = []
#vars
emojid = ""
scree = turtle.Screen()
turt = turtle.Turtle()
checknum = 0
tilr = 0
#code
print('ait broski, veldu tölu sem er á milli 1 og 100')
#for i in range(random.randint(5, 60)):
#    print(random.randint(1,300))
#   time.sleep(0.5)
while checknum == 0:
    corr = random.randint(1,100)
    usinp = int(input(''))
    alltilr.append(tilr)
#    int(usinp)
    if tilr >= 20:
        emojid = emojis.encode(":skull:")
    if usinp == corr:
        print('vel gert!')
        checknum = checknum + 1
        print(f"þetta tók {tilr} tilraunir {emojid}")
    else:
        print('damn bro ekki nogu gott, veldu aðra')
        print('tilraunir sem þú hefur prófað:')
        print(alltilr)
        tilr = tilr + 1

drawSpiral(turt, 80)
scree.exitonclick()