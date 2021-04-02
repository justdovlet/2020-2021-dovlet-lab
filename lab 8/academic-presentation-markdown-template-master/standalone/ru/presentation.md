---
## Front matter
lang: ru-RU
title: Презентация лабораторной работы 8
author: |
	Оразклычев Довлет\inst{1}
institute: |
	\inst{1}RUDN University, Moscow, Russian Federation
date: 2020-2021 г., Москва

## Formatting
mainfont: Times New Roman
romanfont: Times New Roman
sansfont: Times New Roman
monofont: Times New Roman
toc: false
slide_level: 2
theme: metropolis
header-includes:
- \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
- '\makeatletter'
- '\beamer@ignorenonframefalse'
- '\makeatother'
aspectratio: 43
section-titles: true
---

# Знакомство с задачей

## Задание

![Задание](image/1.png){ #fig:001 width=70% }



## Добавление библиотек и переменных

```Python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

p_cr = 20
tau1 = 10
p1 = 9
tau2 = 16
p2 = 7
V = 10
q = 1
```

## Функции
```Python
t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)
v0 = [2, 1]

def f(x, t):
    dx1 = (c1 / c1) * x[0] - ((a1 / c1) + 0.0015) * x[0] * x[0] - (b / c1) * x[0] * x[1]
    dx2 = (c2 / c1) * x[1] - (a2 / c1) * x[1] * x[1] - (b / c1) * x[0] * x[1]
    return dx1, dx2
```
## Находим значения для графика

```Python
yf = odeint(f, v0, t)
```

## Вывод на экран
```Python
plt.figure(figsize=(10, 10))
plt.plot(t, yf)
plt.show()
```
## График №1

![График №1](image/2.png){ #fig:002 width=70% }

## График №2

![График №2](image/3.png){ #fig:003 width=70% }
