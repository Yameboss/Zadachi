import sys
import math


def calculate_position(center_x, center_y, radius, point_x, point_y):
    # Вычисляем расстояние от точки до центра окружности
    distance = math.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)

    # Определяем положение точки относительно окружности
    if distance < radius:
        return 1  # точка внутри окружности
    elif math.isclose(distance, radius, abs_tol=1e-9):
        return 0  # точка на окружности
    else:
        return 2  # точка снаружи окружности


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    try:
        # Чтение данных окружности из файла
        with open(circle_file, 'r') as file:
            circle_data = file.readlines()
        center_x, center_y = map(float, circle_data[0].strip().split())
        radius = float(circle_data[1].strip())

        # Чтение координат точек из файла
        with open(points_file, 'r') as file:
            points_data = file.readlines()

        # Вычисление и вывод положения каждой точки
        for point in points_data:
            point_x, point_y = map(float, point.strip().split())
            position = calculate_position(center_x, center_y, radius, point_x, point_y)
            print(position)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()