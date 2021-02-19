---
## Front matter
lang: ru-RU
title: Презентация лабораторной работы №2
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

# Знакомство с задачей о погоне

## Задача о погоне

Задача преследования браконьеров береговой охраной. На море в тумане катер береговой охраны преследует лодку браконьеров. Через определенный промежуток времени туман рассеивается, и лодка обнаруживается на расстоянии k км от катера. Затем лодка снова скрывается в тумане и уходит прямолинейно в неизвестном направлении. Известно, что скорость катера в 2 раза больше скорости браконьерской лодки. Необходимо определить по какой траектории необходимо двигаться катеру, чтоб нагнать лодку.


## Стратегия

 - Прямолинейно движемся к полюсу до тех пор пока не окажемся на одном расстоянии от полюса.
 - Отплываем **ОТ** полюса на той же скорости что и лодка, а оставшуюся скорость направляем для вращения вокруг полюса. 



## Движение к полюсу


![](image/1.png){ #fig:001 width=70% }

## Движение от полюса к лодке

![](image/2.png){ #fig:002 width=70% }


## {.standout}

Спасибо за внимание!
