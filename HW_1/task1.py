# 1. Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def bubble_sort(lst):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = True
    return lst


lst = [2, 7, 3, 4, 9, 5, 6, 8, 1]
print(bubble_sort(lst))
