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
print('Изменение типа на float64', ar_change_type)
ar_change_type.dtype = np.int64
print('Возврат на int64', ar_change_type, **ARG_)

ar_for_max_min = np.arange(5, 10)
max_ = np.max(ar_for_max_min)
min_ = np.min(ar_for_max_min)
mean_ = np.mean(ar_for_max_min)
print('Максимум, Минимум, средне арифметическое', max_, min_, mean_, **ARG_)

random_ar = np.random.rand(5)
print('Массив из 5 рандомных элементов (от 0 до 1)', random_ar, **ARG_)

random_randint = np.random.randint(50, 60, (3, 2))
print('Матрица с рандомными элементами от 50 до 60', random_randint, **ARG_)

ar_shuffle = np.arange(10)
np.random.shuffle(ar_shuffle)
print('Перетасовка массива от 0 до 10', ar_shuffle, **ARG_)

random_for_set = np.random.randint(5, 10, 10)
print(f'Создание множества из {random_for_set}')
set_1 = np.unique(random_for_set, return_counts=True)
print(f'Количество повторений {set_1}')
set_2 = np.unique(random_for_set, return_index=True)
print(f'Индекс первого вхождения {set_2}')
set_3 = np.unique(random_for_set, return_inverse=True)
print(f'Массив для восстановления {set_3}', **ARG_)

ar1 = np.arange(10)
print(f'Массив {ar1}')
print(f'Тип элементов {ar1.dtype}')
print(f'Длина {ar1.size}')
print(f'Количество осей {ar1.ndim}')
print(f'Узнать размерность {ar1.shape}')
print(f'Задать размерность {ar1.reshape((2, 5)).shape}')
