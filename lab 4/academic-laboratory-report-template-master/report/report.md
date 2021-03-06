---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе 4"
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

Построить модели осциалятора

# Задание

(рис. -@fig:001)

![Задание лабораторной работы](image/1.png){ #fig:001 width=70% }



# Выполнение лабораторной работы

Для начала мы импортируем библиотеки для построения кода и вводим наши переменные: 

```Python
import numpy as np
import math
import matplotlib.pyplot as plt

from scipy.integrate import odeint

w = math.sqrt(6)
g = 3

t0 = 0
tmax = 50
dt = 0.05

```

Теперь мы создаем список значений t, которое мы будем использовать чтобы вычислять поточечно значения "Численность армии":

```Python
t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)
```
Обратите внимаение, что я также добавил элемент tmax в конец списка. Дело в том, что функция np.arange заполняет от нуля до tmax - dt, поэтому надо добавлять еще один элемент отдельно.


Теперь создаем непрерывные функции и систему уравнений:
```Python
def p(t):
    return (math.sin(t*0.5))

def syst(x, t):
    return x[1], -w * w * x[0] - g * x[1] - p(t)
```

Создаем вектор значений наших данных и запускаем команду odeint, которая найдет значения поточечно.

```Python
v0 = (-1, 1)

yf = odeint(syst, v0, t)

x = []
y = []

for i in range(len(yf)):
    x.append(yf[i][0])
    y.append(yf[i][1])
```

Теперь создаем график и выводим на экран.
график будет красного цвета с обозначением "x". Размер графика 10 на 10 единиц.

```Python

plt.figure(figsize=(10, 10))
plt.plot(x, y, 'r', label='x')
plt.show()

```

И получаем: (рис. -@fig:002)

![График первого осцилятора](image/2.png){ #fig:002 width=70% }



(рис. -@fig:003)

![График второго осцилятора](image/3.png){ #fig:003 width=70% }



(рис. -@fig:004)

![График третьего осцилятора](image/4.png){ #fig:004 width=70% }


Код на Python для случая 1:
```Python
import numpy as np
import math
import matplotlib.pyplot as plt

from scipy.integrate import odeint

w = 8
g = 0.00

t0 = 0
tmax = 45
dt = 0.05

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)


def p(t):
    #return (math.sin(t*0.5))
    return 0


def syst(x, t):
    return x[1], -w * w * x[0] - g * x[1] - p(t)


v0 = (-1, 0)

yf = odeint(syst, v0, t)

x = []
y = []

for i in range(len(yf)):
    x.append(yf[i][0])
    y.append(yf[i][1])

zero = []
for i in range(len(t)):
    zero = np.append(zero, 0)

plt.figure(figsize=(10, 10))
plt.plot(x, y, 'r', label='x')
plt.show()



```

Код на Python для случая 2:
```Python
import numpy as np
import math
import matplotlib.pyplot as plt

from scipy.integrate import odeint

w = 3
g = 4.00

t0 = 0
tmax = 45
dt = 0.05

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)


def p(t):
    #return (math.sin(t*0.5))
    return 0


def syst(x, t):
    return x[1], -w * w * x[0] - g * x[1] - p(t)


v0 = (-1, 0)

yf = odeint(syst, v0, t)

x = []
y = []

for i in range(len(yf)):
    x.append(yf[i][0])
    y.append(yf[i][1])

zero = []
for i in range(len(t)):
    zero = np.append(zero, 0)

plt.figure(figsize=(10, 10))
plt.plot(x, y, 'r', label='x')
plt.show()

```

Код на Python для случая 3:
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

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)


def p(t):
    return (math.sin(t*0.5))

def syst(x, t):
    return x[1], -w * w * x[0] - g * x[1] - p(t)


v0 = (-1, 0)

yf = odeint(syst, v0, t)

x = []
y = []

for i in range(len(yf)):
    x.append(yf[i][0])
    y.append(yf[i][1])

plt.figure(figsize=(10, 10))
plt.plot(x, y, 'r', label='x')
plt.show()


```
# Выводы

Построили код на Python для решения и вывода на экран моделей осциляторов.


# Ответы на вопросы

Вопросы:

1. Запишите простейшую модель гармонических колебаний

2. Дайте определение осциллятора

3. Запишите модель математического маятника

4. Запишите алгоритм перехода от дифференциального уравнения второго порядка

к двум дифференциальным уравнениям первого порядка

5. Что такое фазовый портрет и фазовая траектория?


Ответы:

1. sin(x)

2. Система, которая при выведении её из положения равновесия испытывает действие возвращающей силы

3. ¨ф+w^2^~0~ф=0

4. Дважды интегрируем и получаем общее решение

5. 
a) Геометрическое представление траекторий динамической системы на фазовой плоскости

b) Проекция интегральной кривой
