import turtle


def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    file = open("draw_step.txt", "r")

    for line in file:
        text = line.strip()
        command_list = text.split(",")
        command = command_list[0]

        if command == "goto":
            x = float(command_list[1])
            y = float(command_list[2])
            width = float(command_list[3])
            color = command_list[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)

        elif command == 'circle':
            radius = float(command_list[1])
            width = float(command_list[2])
            color = command_list[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)

        elif command == "beginfill":
            color = command_list[1].strip()
            t.fillcolor(color)
            t.begin_fill()

        elif command == "endfill":
            t.end_fill()

        elif command == "penup":
            t.penup()

        elif command == "pendown":
            t.pendown()

        else:
            print("Unknow command found in file: ", command)

    file.close()
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed!")


if __name__ == "__main__":
    main()
