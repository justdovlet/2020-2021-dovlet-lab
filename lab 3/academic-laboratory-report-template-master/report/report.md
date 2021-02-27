---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе 3"
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

Решить задачу о погоне

# Задание

Между страной Х и страной У идет война. Численность состава войск
исчисляется от начала войны, и являются временными функциями
x(t) и y(t). В начальный момент времени страна Х имеет армию численностью 50 000 человек, а в распоряжении страны У армия численностью в 69 000 человек. Для упрощения
модели считаем, что коэффициенты a, b, c, h постоянны. Также считаем P(t) и Q(t) непрерывные функции.

Постройте графики изменения численности войск армии Х и армии У для следующих случаев: (рис. -@fig:001)

![Модели боевых действий](image/1.png){ #fig:001 width=70% }



# Выполнение лабораторной работы

Для начала мы импортируем библиотеки для построения кода и вводим наши переменные: 

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

График будет таков: "Время" / "Численность армии"

Теперь мы создаем список значений t, которое мы будем использовать чтобы вычислять поточечно значения "Численность армии":

```Python
t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)
```
Обратите внимаение, что я также добавил элемент tmax в конец списка. Дело в том, что функция np.arange заполняет от нуля до tmax - dt, поэтому надо добавлять еще один элемент отдельно.


Теперь создаем непрерывные функции и систему уравнений:
```Python
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

Создаем вектор значений наших данных и запускаем команду odeint, которая найдет значения "Численность армии" поточечно.

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
Создаем zero чтобы видеть полосу, где численность армии будет равняться нулю. Когда один из графиков пересечется с ним, то это будет значить, что кол-во людей в армии достигла нуля.


Теперь создаем график и выводим на экран.

Численность армии x будет "r", т.е. красным.
Численность армии y будет "g", т.е. зеленым.
Легенды ставим на правых вверхний угол. 
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

И получаем: (рис. -@fig:002)

![График модели первых боевых действий](image/2.png){ #fig:002 width=70% }



(рис. -@fig:002)

![График модели вторых боевых действий](image/3.png){ #fig:003 width=70% }


Код на Scilab для случая 1:
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

Код на Scilab для случая 2:
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

a = 0.12
b = 0.51
c = 0.30
h = 0.61

tmax = 5
dt = 0.05

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def p(t):
    return (math.sin(t*20))

def q(t):
    return (math.cos(t*13))

def syst(f,t):
    x = f[0]
    y = f[1]
    dxdt = -a*x - b*y + p(t)
    dydt = -c*x*y - h*y + q(t)
    return (dxdt,dydt)

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


plt.figure(figsize = (20, 15))
plt.plot(t, zero, 'b')
plt.plot(t, x, 'r', label = 'x')
plt.plot(t, y, 'g', label = 'y')
print (y)
plt.ylabel('Численность армии')
plt.xlabel('Время')
plt.title('Модель боевых действий №1')
plt.legend(loc ='upper right')


plt.show()
```
# Выводы

Построили код на Python для решения и вывода на  экран моделей боевых действий.
