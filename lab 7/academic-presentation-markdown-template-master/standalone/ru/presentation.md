---
## Front matter
lang: ru-RU
title: Презентация лабораторной работы 7
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

N = 777
x0 = 1
t0 = 0
tmax = 30
dt = 0.1
```

## Функции
```Python
t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def k(t):
    return 0.99
def p(t):
    return 0.00012
def f(x, t):
    return (k(t) + p(t)*x)*(N-x)
```
## Находим значения для графика

```Python
yf = odeint(f, x0, t)
```

## Вывод на экран
```Python
plt.figure(figsize=(10, 10))
plt.plot(t, yf, 'r', label='S(t)')
plt.show()
```
## График №1

![График №1](image/2.png){ #fig:002 width=70% }

## График №2

![График №2](image/3.png){ #fig:003 width=70% }

## График №3

![График №3](image/4.png){ #fig:004 width=70% }
