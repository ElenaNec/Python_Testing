# Задание 2
# Напишите программу, которая рассчитывает положение точки относительно
# окружности.
# Координаты центра окружности и его радиус считываются из файла 1.
# Пример:
# 1 1
# 5
# Координаты точек считываются из файла 2.
# Пример:
# 0 0
# 1 6
# 6 6
# Вывод для данных примеров файлов:
# 1
# 0
# 2
# Пути к файлам передаются программе в качестве аргументов!
# ● файл с координатами и радиусом окружности - 1 аргумент;
# ● файл с координатами точек - 2 аргумент;
# ● координаты - рациональные числа в диапазоне от 10-38 до 1038;
# ● количество точек от 1 до 100;
# ● вывод каждого положения точки заканчивается символом новой строки;
# ● соответствия ответов:
# ○ 0 - точка лежит на окружности
# ○ 1 - точка внутри
# ○ 2 - точка снаружи.
# Вывод программы в консоль.

import sys


def read_circle(filename):
    try:
        with open(filename, 'r') as file:
            x, y = map(float, file.readline().split())
            radius = float(file.readline())
        return x, y, radius
    except FileNotFoundError:
        print(f"File {filename} not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error reading data from {filename}.")
        sys.exit(1)


def read_points(filename):
    points = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                x, y = map(float, line.split())
                points.append((x, y))
        return points
    except FileNotFoundError:
        print(f"File {filename} not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error reading data from {filename}.")
        sys.exit(1)


def point_position(x_center, y_center, radius, x_point, y_point):
    distance_squared = (x_point - x_center) ** 2 + (y_point - y_center) ** 2
    if distance_squared < radius ** 2:
        return 1  # Точка внутри окружности
    elif distance_squared > radius ** 2:
        return 2  # Точка снаружи окружности
    else:
        return 0  # Точка на окружности


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use the format: python task2.py circle_file points_file")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    x_center, y_center, radius = read_circle(circle_file)
    points = read_points(points_file)

    for point in points:
        position = point_position(x_center, y_center, radius, *point)
        print(position)
