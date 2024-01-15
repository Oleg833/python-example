import turtle

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)

def draw_complete_snowflake(turtle, order, size):
    for _ in range(3):
        koch_snowflake(turtle, order, size)
        turtle.right(120)

def main():
    # Налаштування туртлу
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Koch Snowflake")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.color("blue")
    snowflake_turtle.width(2)

    # Початкові координати та орієнтація туртлу
    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()

    # Виклик функції для генерації сніжинки Коха
    draw_complete_snowflake(snowflake_turtle, 2, 300)

    # Закриваємо вікно при кліку
    screen.exitonclick()

if __name__ == "__main__":
    main()
