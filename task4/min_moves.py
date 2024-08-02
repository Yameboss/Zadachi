import sys


def read_numbers_from_file(file_path):
    """Читает числа из файла и возвращает их в виде списка целых чисел."""
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers


def find_median(nums):
    """Находит медиану в отсортированном списке чисел."""
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        # Если количество элементов четное, медиана может быть любым из двух средних чисел.
        return nums[n // 2]  # Можно выбрать любое значение из двух.


def calculate_moves(nums, median):
    """Вычисляет минимальное количество ходов для приведения всех чисел к медиане."""
    return sum(abs(num - median) for num in nums)


def main(file_path):
    nums = read_numbers_from_file(file_path)
    median = find_median(nums)
    moves = calculate_moves(nums, median)
    print(moves)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <numbers.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)