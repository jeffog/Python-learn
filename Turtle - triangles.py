import turtle
def draw_triangle():
    jeff = turtle.Turtle()
    jeff.shape("turtle")
    jeff.color("blue")
    jeff.speed(10)

    angle = 30
    
    face = 0
    while (face < 36):
        jeff.right(10)
        face = face + 1
        c = 0
        while (c < 4):
            a = c % 2
            jeff.forward(100)
            jeff.right(angle + angle * 4 * a)
            c = c + 1

draw_triangle()
