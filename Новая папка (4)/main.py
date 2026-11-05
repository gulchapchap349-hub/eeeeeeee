import turtle
import random

# Настройки экрана
screen = turtle.Screen()
screen.bgcolor("#1a1a1a")  # Темный фон
screen.title("Генеративное фрактальное дерево")

t = turtle.Turtle()
t.pensize(2)
t.speed(0)
t.left(90)
t.up()
t.backward(200)
t.down()
t.color("#2ed573")  # Зеленый цвет ветвей

def draw_tree(branch_len, t):
    if branch_len > 5:
        # Устанавливаем цвет в зависимости от длины (чем ближе к концу, тем зеленее)
        if branch_len < 20:
            t.color("#2ed573")
        else:
            t.color("#8e44ad") # Фиолетовый ствол
            
        # Случайные углы и длина для естественного вида
        angle1 = random.randint(15, 45)
        angle2 = random.randint(15, 45)
        sub_len = branch_len - random.randint(10, 20)
        
        # Рисуем ветвь
        t.forward(branch_len)
        
        # Правая ветка
        t.right(angle1)
        draw_tree(sub_len, t)
        
        # Левая ветка
        t.left(angle1 + angle2)
        draw_tree(sub_len, t)
        
        # Возвращаемся назад
        t.right(angle2)
        t.up()
        t.backward(branch_len)
        t.down()

# Запуск генерации
draw_tree(100, t)
turtle.done()
