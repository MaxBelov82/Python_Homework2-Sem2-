# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime
# (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number


def fill_list(diap):
    target_list = []
    for i in range(diap):
        target_list.append(randint(-diap, diap))
    return target_list


def check_list(num, diap, target_list):
    if -diap < num < diap:
        for i in target_list:
            if i == num:
                print("Yes")
                break
        else:
            print("No")
    else:
        print("число вне пределов ")


diapazon = InputNumbers("Введите диапазон (от -х до +х) и он же размер списка: ")

target_list = fill_list(diapazon)

print(target_list)

check_number = InputNumbers("Введите проверяемое число: ")

check_list(check_number, diapazon + 1, target_list)