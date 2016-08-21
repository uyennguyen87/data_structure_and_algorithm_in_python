import turtle


def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    file = open("draw_steps.txt", "r")

    command = file.readline().strip()

    while command != "":
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)

        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)

        elif command == "beginfill":
            color = file.readline().strip()
            t.fillcolor(color)
            t.begin_fill()

        elif command == "endfill":
            t.end_fill()

        elif command == "penup":
            t.penup()

        elif command == "pendown":
            t.pendown()

        else:
            print("Unknown command found in file:", command)

        command = file.readline().strip()

    file.close()
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")


if __name__ == "__main__":
    main()
