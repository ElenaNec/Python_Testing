# Задание 4
# Дан массив целых чисел nums.
# Напишите программу, выводящую минимальное количество ходов, требуемых для
# приведения всех элементов к одному числу.
# За один ход можно уменьшить или увеличить число массива на 1.
# Пример:
# nums = [1, 2, 3]
# Решение: [1, 2, 3] => [2, 2, 3] => [2, 2, 2].
# Минимальное количество ходов: 2.
# Элементы массива читаются из файла, переданного в качестве аргумента
# командной строки!
# Пример:
# На вход подаётся файл с содержимым:
# 1
# 10
# 2
# 9
# Вывод в консоль: 16


def min_moves(nums):
    mean = sum(nums) // len(nums) # вычисляет среднее значение всех чисел в списке
    moves = 0
    for num in nums:
        moves += abs(num - mean)  # вычисляет модуль разницы между числом из списка и средним значением
    return moves


def run_program():
    array_file = input('Input path "array_file": ')
    try:
        with open(array_file, 'r') as f:
            nums = [int(line.strip()) for line in f]
    except FileNotFoundError:
        print("File not found.")
        return

    moves = min_moves(nums)
    print(moves)


if __name__ == "__main__":
    run_program()
