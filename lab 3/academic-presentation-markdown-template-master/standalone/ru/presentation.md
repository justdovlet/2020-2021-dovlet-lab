---
## Front matter
lang: ru-RU
title: Презентация лабораторной работы 3
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

# Знакомство с задачей о боевых действиях

## Задание

Постройте графики изменения численности войск армии Х и армии У для следующих случаев: (рис. -@fig:001)

![Модели боевых действий](image/1.png){ #fig:001 width=70% }



## Добавление библиотек и переменных

```Python
import numpy as np
import pandas as pd
import scipy as sp
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint
x0 = 50000
y0 = 69000
t0 = 0
a = 0.34
b = 0.72
c = 0.89
h = 0.43
tmax = 3
dt = 0.05
```

## Функции
```Python
t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def p(t):
    return (math.sin(t+10))

def q(t):
    return (math.cos(t+20))

def syst(f,t):
    x = f[0]
    y = f[1]
    dxdt = -a*x - b*y + p(t)
    dydt = -c*x - h*y + q(t)
    return (dxdt,dydt)
```
## Находим значения для Численности армии 

```Python
v0 = (x0, y0)

yf = odeint(syst, v0, t)

x = []
y = []

for i in range(len(yf)):
    x.append(yf[i][0])
    y.append(yf[i][1])

zero = []
for i in range (len(t)):
    zero = np.append(zero,0)
```

## Вывод на экран
```Python
plt.figure(figsize = (20, 15))
plt.plot(t, zero, 'b')
plt.plot(t, x, 'r', label = 'x')
plt.plot(t, y, 'g', label = 'y')
plt.ylabel('Численность армии')
plt.xlabel('Время')
plt.title('Модель боевых действий №1')
plt.legend(loc ='upper right')

plt.show()
```
## График №1

![График модели первых боевых действий](image/2.png){ #fig:002 width=70% }

## График №2

![График модели вторых боевых действий](image/3.png){ #fig:003 width=70% }


## {.standout}

Благодарю за внимание.
