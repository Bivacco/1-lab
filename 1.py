#Вариант 18. Натуральные числа. Выводит на экран числа, убирая нечетные цифры в каждом четном по порядку числе. Убранные цифры печать отдельно прописью.
def remove_odd_digits(num):
    even_nums = [int(x) for x in str(num) if int(x) % 2 == 0]
    removed_nums = [int(x) for x in str(num) if int(x) % 2 != 0]
    print(f"Из числа {num} удалены нечетные цифры: {' '.join(str(x) for x in removed_nums)}")
    return int(''.join(str(x) for x in even_nums))

def process_sequence(sequence):
    current_num = ""
    found_number = False
    for char in sequence:
        if char.isdigit():
            current_num += char
        else:
            if current_num:
                num = int(current_num)
                if num % 2 == 0:
                    found_number = True
                    result = remove_odd_digits(num)
                    print(f"Число после удаления нечетных цифр: {result}\n")
                current_num = ""
    if not found_number:
        print("Файл пустой или не содержит натуральных чисел.")

# Чтение последовательности из файла
with open('sequence.txt', 'r') as file:
    sequence = file.read()

process_sequence(sequence)


# Эмулируем бесконечную последовательность символов
sequence = "abc;123;456;def;789;012;ghi"

process_sequence(sequence)
