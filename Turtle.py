import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    jeff = turtle.Turtle()
    jeff.shape("turtle")
    jeff.speed(1)
    jeff.color("yellow")

    c = 0
    while (c < 360):
        jeff.right(1)
        jeff.speed(c)
        c = c + 1
        x = 0
        while (x < 4):
            jeff.forward(100)
            jeff.right(90)
            x = x + 1

    

draw_square()

