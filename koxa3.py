import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def draw_complete_snowflake(turtle, order, size):
    for _ in range(3):
        koch_snowflake(turtle, order, size)
        turtle.right(120)

def main():
    # Запитати користувача про рівень рекурсії
    try:
        recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    # Ініціалізувати вікно та черепаху
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.color("blue")
    snowflake_turtle.width(2)
    snowflake_turtle.speed(2)

    # Початкові координати та орієнтація туртлу
    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()

    # Викликати функцію для малювання сніжинки Коха
    draw_complete_snowflake(snowflake_turtle, recursion_level, 300)

    # Закрити вікно при кліку на нього
    window.exitonclick()

if __name__ == "__main__":
    main()
