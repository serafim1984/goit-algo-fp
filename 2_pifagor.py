import turtle

def draw_pythagoras_tree(t, length, angle, iterations):
    if iterations == 0 or length < 0.01:
        return

    t.forward(length)
    t.left(angle)
    draw_pythagoras_tree(t, length/1.5, angle, iterations-1)
    t.right(2*angle)
    draw_pythagoras_tree(t, length/1.5, angle, iterations-1)
    t.left(angle)
    t.backward(length)

def main():
    # Setup turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Set maximum speed

    # Move turtle to starting position
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    # Draw Pythagoras tree with 3 iterations
    draw_pythagoras_tree(t, 100, 45, 8)

    # Hide turtle and display result
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()