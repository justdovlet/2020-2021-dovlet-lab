---
## Front matter
lang: ru-RU
title: Презентация лабораторной работы 4
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

# Знакомство с задачей об осциляторах

## Задание

Постройте графики осциляторов: (рис. -@fig:001)

![Задание](image/1.png){ #fig:001 width=70% }



## Добавление библиотек и переменных

```Python
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

w = 6
g = 3.00

t0 = 0
tmax = 45
dt = 0.05
```

## Функции
```Python
t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)


def p(t):
    return (math.sin(t*0.5))

def syst(x, t):
    return x[1], -w * w * x[0] - g * x[1] - p(t)
```
## Находим значения для графика осцилятора

```Python
v0 = (-1, 0)

yf = odeint(syst, v0, t)

x = []
y = []

for i in range(len(yf)):
    x.append(yf[i][0])
    y.append(yf[i][1])
```

## Вывод на экран
```Python
plt.figure(figsize=(10, 10))
plt.plot(x, y, 'r', label='x')
plt.show()
```
## График №1

![График №1](image/2.png){ #fig:002 width=70% }


## График №2

![График №2](image/3.png){ #fig:003 width=70% }


## График №3

![График №3](image/4.png){ #fig:004 width=70% }

