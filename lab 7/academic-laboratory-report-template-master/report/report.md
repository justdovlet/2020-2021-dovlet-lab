---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе 7"
subtitle: "НФИбд-02-18"
author: "Оразклычев Довлет"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Постройте графики изменения числа особей в каждой из трех групп.

# Задание

![Задание лабораторной работы](image/1.png){ #fig:001 width=70% }


# Выполнение лабораторной работы

Для начала мы импортируем библиотеки для построения кода и вводим наши переменные: 

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

Теперь мы создаем список значений t, которое мы будем использовать чтобы вычислять поточечно значения "Численность армии":

```Python
t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)
```
Обратите внимаение, что я также добавил элемент tmax в конец списка. Дело в том, что функция np.arange заполняет от нуля до tmax - dt, поэтому надо добавлять еще один элемент отдельно.


Теперь создаем систему уравнений:
```Python
def k(t):
    return 0.99
def p(t):
    return 0.00012
def f(x, t):
    return (k(t) + p(t)*x)*(N-x)
```

Запускаем команду odeint, которая найдет значения поточечно.

```Python
yf = odeint(f, x0, t)
```

Теперь создаем график и выводим на экран.
график будет красного цвета с обозначением "x". Размер графика 10 на 10 единиц.

```Python
plt.figure(figsize=(10, 10))
plt.plot(t, yf, 'r', label='S(t)')
plt.show()
```

И получаем:

![Случай 1](image/2.png){ #fig:002 width=70% }


![Случай 2](image/3.png){ #fig:003 width=70% }


![Случай 3](image/4.png){ #fig:004 width=70% }




Код на Python для графика 1:
```Python
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint


N = 777
x0 = 1

t0 = 0
tmax = 30
dt = 0.1

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def k(t):
    return 0.99
def p(t):
    return 0.00012
def f(x, t):
    return (k(t) + p(t)*x)*(N-x)


yf = odeint(f, x0, t)


plt.figure(figsize=(10, 10))
plt.plot(t, yf, 'r', label='S(t)')
plt.show()
```

Код на Python для графика 2:
```Python
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint


N = 777
x0 = 1

t0 = 0
tmax = 30
dt = 0.1

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def k(t):
    return 0.000067


def p(t):
    return 0.38


def f(x, t):
    return (k(t) + p(t)*x)*(N-x)


yf = odeint(f, x0, t)


plt.figure(figsize=(10, 10))
plt.plot(t, yf, 'r', label='S(t)')
plt.show()

```

Код на Python для графика 3:
```Python
import numpy as np
import matplotlib.pyplot as plt
import math

from scipy.integrate import odeint


N = 777
x0 = 1

t0 = 0
tmax = 30
dt = 0.1

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def k(t):
    return 0.6*math.sin(4*t)


def p(t):
    return 0.1*math.cos(2*t)


def f(x, t):
    return (k(t) + p(t)*x)*(N-x)


yf = odeint(f, x0, t)


plt.figure(figsize=(10, 10))
plt.plot(t, yf, 'r', label='S(t)')
plt.show()
```

# Вывод

Построили код на Python для решения и вывода на экран графиков эффективности рекламы для 3 случаев.

