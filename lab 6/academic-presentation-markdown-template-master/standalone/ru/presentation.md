---
## Front matter
lang: ru-RU
title: Презентация лабораторной работы 6
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
a = 0.17
b = 0.046
R0 = 12
I0 = 212
N = 12000
S0 = N - I0 - R0
t0 = 0
tmax = 200
dt = 0.01
```

## Функции
```Python
t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

# I0 < I*
def syst(x, t):
    dx1 = 0
    dx2 = -b * x[1]
    dx3 = b * x[1]
    return dx1, dx2, dx3
```
## Находим значения для графика

```Python
v0 = (S0, I0, R0)
yf = odeint(syst, v0, t)
y1 = []
y2 = []
y3 = []
for i in range(len(yf)):
    y1.append(yf[i][0])
    y2.append(yf[i][1])
    y3.append(yf[i][2])
```

## Вывод на экран
```Python
plt.figure(figsize=(10, 10))
plt.plot(t, y1, 'r', label='S(t)')
plt.plot(t, y2, 'b', label='I(t)')
plt.plot(t, y3, 'g', label='R(t)')
plt.legend( loc = "upper right")
plt.show()
```
## График №1

![График №1](image/2.png){ #fig:002 width=70% }

## График №2

![График №2](image/3.png){ #fig:003 width=70% }

