import turtle

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order-1, size/3)
            turtle.left(angle)

# Виклик функції для побудови кривої на третьому рівні
my_turtle = turtle.Turtle()
my_turtle.speed(3)
koch_snowflake(my_turtle, 3, 300)

turtle.done()
