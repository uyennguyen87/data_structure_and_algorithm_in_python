from python_programming_101.accumulator.PyList import PyList
from python_programming_101.polymorphism.BeginFillCommand import BeginFillCommand
from python_programming_101.polymorphism.CircleCommand import CircleCommand
from python_programming_101.polymorphism.EndFillCommand import EndFillCommand
from python_programming_101.polymorphism.GoToCommand import GoToCommand
from python_programming_101.polymorphism.PenDownCommand import PenDownCommand
from python_programming_101.polymorphism.PenUpCommand import PenUpCommand

if __name__ == "__main__":
    import turtle
    t = turtle.Turtle()
    screen = t.getscreen()
    file_name = "draw_steps.txt"
    file = open(file_name, "r")

    graphicsCommands = PyList()

    command = file.readline().strip()

    while command != "":
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)

        elif command == "circle" :
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = CircleCommand(radius, width, color)

        elif command == "beginfill":
            color = file.readline().strip()
            cmd = BeginFillCommand(color)

        elif command == "endfill":
            cmd = EndFillCommand()

        elif command == "penup":
            cmd = PenUpCommand()

        elif command == "pendown":
            cmd = PenDownCommand()

        else:
            raise RuntimeError("unknow Coomand: " + command)

        graphicsCommands.append(cmd)
        command = file.readline().strip()

    for cmd in graphicsCommands:
        cmd.draw(t)

    file.close()
    t.ht()
    screen.exitonclick()
    print("Pragram Execution Completed!")