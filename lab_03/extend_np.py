import numpy as np
ARG_ = {'sep': '\n', 'end': '\n\n'}


ar_one = np.arange(10)
ar_two = np.arange(5, 10)
ar_three = np.arange(5, 10, 0.5)
print(ar_one, ar_two, ar_three, **ARG_)

lin_ar = np.linspace(0, 100, 5)
print(lin_ar, **ARG_)

zero_ar = np.zeros(5)
one_ar = np.ones(5)
print(zero_ar, one_ar, **ARG_)

dia_ar = np.diag([2, 7, 8])
print(dia_ar, **ARG_)

rand_ar = np.empty((3, 3), 'int16')
custom_ar = np.full((4, 4), 2)
print(rand_ar, custom_ar, **ARG_)

ar_change_type = np.arange(10)
ar_change_type.dtype = np.float64
print(ar_change_type)
ar_change_type.dtype = np.int64
print(ar_change_type, **ARG_)

