import math


def correlation_pearson(array_1, array_2):
    if len(array_1) != len(array_2):
        raise ValueError("Массивы разной длины")

    n = len(array_1)

    average_x = sum(array_1) / n
    average_y = sum(array_2) / n

    variance_x = sum([(xi - average_x) ** 2 for xi in array_1]) / float(len(array_1))
    variance_y = sum([(yi - average_y) ** 2 for yi in array_2]) / float(len(array_2))

    covariance = sum([(xi - average_x) * (yi - average_y) for xi, yi in zip(array_1, array_2)]) / float(len(array_1))
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


array_1 = [13, 8, 3, 16, 1, 45]
array_2 = [11, 2, 47, 15, 32, 21]

correlation = round(correlation_pearson(array_1, array_2), 3)
print(f"Корреляция Пирсона: {correlation}")
