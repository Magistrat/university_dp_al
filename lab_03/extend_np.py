import numpy as np
ARG_ = {'sep': '\n', 'end': '\n\n'}


ar_one = np.arange(10)
ar_two = np.arange(5, 10)
ar_three = np.arange(5, 10, 0.5)
print('Создание массивов через arange', ar_one, ar_two, ar_three, **ARG_)

lin_ar = np.linspace(0, 100, 5)
print('Создание массивов через linspace', lin_ar, **ARG_)

zero_ar = np.zeros(5)
one_ar = np.ones(5)
print('Создание массивов через zeros и ones', zero_ar, one_ar, **ARG_)

dia_ar = np.diag([2, 7, 8])
print('Создание матрицы через диагональ', dia_ar, **ARG_)

rand_ar = np.empty((3, 3), 'int16')
custom_ar = np.full((4, 4), 2)
print('Создание случайных матриц через empty и full', rand_ar, custom_ar, **ARG_)

ar_change_type = np.arange(10)
ar_change_type.dtype = np.float64
print('Изменение типа', ar_change_type)
ar_change_type.dtype = np.int64
print('Изменение типа', ar_change_type, **ARG_)

ar_for_max_min = np.arange(5, 10)
max_ = np.max(ar_for_max_min)
min_ = np.min(ar_for_max_min)
mean_ = np.mean(ar_for_max_min)
print('Максимум, Минимум, средне арифметическое', max_, min_, mean_, **ARG_)

