import turtle
jeff = turtle.Turtle()
jeff.shape("turtle")
jeff.speed(10)
jeff.penup()
jeff.setx(-200)
jeff.sety(-200)
jeff.pendown()

c = 1
steps = 10

def draw_triangle():
    jeff.begin_fill()
    for _ in range(3):
        jeff.forward(steps)
        jeff.left(120)
    jeff.end_fill()
    jeff.forward(steps)
   
def draw_big_triangle():
    for _ in range (3):
        for clr in ["pink","gray","purple"]:
            jeff.color(clr)
            draw_triangle()
        jeff.forward(steps)
        jeff.left(120)
 
while (c < 100):
    for _ in range (3):
        draw_big_triangle()
        jeff.forward(steps*4)
    jeff.forward(steps*4)
    jeff.left(120)
    print(c)
    c = c + 1
 
print(jeff.position())
