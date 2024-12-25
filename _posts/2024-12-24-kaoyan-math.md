---
layout: article
title: "考研数学一"
tags: "考研"
category: kaoyan
excerpt_separator: <!--brief-->
permalink: /kaoyan/math
---
整理一下考研数学一的一些知识点，个人感觉还挺全的。
但是对于相关的解题技巧以及解题思路，还得靠多思考多做题。

<!--brief-->
# 函数，极限和连续

## 极限

极限的概念，用$\delta, \varepsilon$语言描述，还有几何意义。（不太重要）

$数列极限=a\iff奇子列极限=偶子列极限=a$

需要注意区分左右极限的：

- 分段函数，包括含绝对值的
- $e^{\infin}$型，包括$\lim\limits_{x\to0}e^{\frac1x},\lim\limits_{x\to\infin}e^{x}$，他们的极限都不存在（左右极限不相等）
- $\arctan\infin$型，包括$\lim\limits_{x\to0}\arctan\frac1x,\lim\limits_{x\to\infin}\arctan x$，极限不存在，左右极限不相等

证明极限存在的两个常用方法：夹逼法，一般是求n项和；单调有界，一般有递推式$x_{n+1}=f(x_n)$。还有什么传奇🐙老师的压缩映射，自行理解

其中，夹逼很经典的例子是：
$$
\lim\limits_{n\to\infin}\sqrt[n]{a_1^n+a_2^n+\dots+a_k^n}=max\{a_i\}
$$
单调有界数列必有极限。步骤：做差/商证单调，数学归纳法证有界，令极限为A，解方程。

压缩映射的核心是构建$|x_{n+1}-A|\leq k^n|x_1-a|$的关系，通常使用导数或者拉格朗日中值定理

几个常用的极限：

| 1                                               | 2                                       | 3                                       |
| ----------------------------------------------- | --------------------------------------- | --------------------------------------- |
| $\lim\limits_{x\to0}\frac{1}{x}(a^{x}-1)=\ln a$ | $\lim\limits_{n\to\infin}\sqrt[n]{n}=1$ | $\lim\limits_{n\to\infin}\sqrt[n]{a}=1$ |
| $1^{\infin}=e^A$                                | 分式除法抓大头                          |                                         |

常用等价无穷小：懒得写，直接背泰勒

## 连续

函数在某点连续：在这个点的极限等于他的值。$\lim\limits_{x\to{x_0}}f(x)=f(x_0)$

间断点：要求在$x_0$的去心邻域内有定义，但在$x_0$不连续。所以0不是$\ln x$的间断点。

初等函数的间断点只可能在  分段函数的分段点处  和  无定义的点

- 第一类（可去，跳跃）--在$x_0$处的左右极限都存在，但不一定相等。
  - 可去，左右极限都存在但不等于函数值
  - 跳跃，左右极限都存在但不相等
- 第二类（无穷，震荡）--在$x_0$处的左右极限至少有一个不存在。
  - 无穷，类似$\tan x$
  - 震荡，类似$\sin \frac1x$在原点。其实在考研数学中，接触到的震荡间断点都是它的变形。但是要注意$x$是趋于无穷还是0.

闭区间上的连续函数的几个性质：听起来很简单，但是在做题中要想到：

- 最值存在，也就是有界
- 介值定理：$\exists \xi\in(a,b),f(\xi)=C.\quad C\in[A,B]\sube[min,max] $
- 零点存在定理。注意是$f(a)f(b)<0$，当不严格小于0时，还要讨论等于0的情况。

# 导数，微分

## 定义

导数定义：$f'(x_0)=\lim\limits_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}=\lim\limits_{h\to 0}\frac{f(x_0+h)-f(x_0)}{h}$

微分：增量$\Delta y=f(x_0+\Delta x)-f(x_0)=A\Delta x+o(\Delta x)$，若A于$\Delta x$无关，则微分${\rm d}y=A\Delta x$，当$\Delta x$是一个小量时，$A=f'(x_0),{\rm d}y=f'(x_0)\Delta x=f'(x_0){\rm d}x$

一元函数的可微和可导是充要条件。可导一定有切线，有切线不一定可导。$f(x)=\sqrt x$

## 导数计算

常用导数：
$$
\begin{aligned}
(\arcsin x)'&=\frac1{\sqrt{1-x^2}}&(\arccos x)'&=-\frac1{\sqrt{1-x^2}}\\
(\arctan x)'&=\frac1{1+x^2}&({\rm arccot} x)'&=-\frac1{1+x^2}

\end{aligned}
$$


Lagrange余项和Peano余项：

拉格朗日余项：$R_n(x)=\frac{1}{(n+1)!}f^{(n+1)}(\xi)(x-x_0)^{n+1},\xi在 x和x_0之间$。要求在闭区间上有n阶连续导数，n+1阶可导。常用于证明区间上的不等式

皮亚诺余项：$R_n(x)=o((x-x_0)^n)$，要求在$x=x_0$处的n阶导数存在，仅能用于$x_0$邻域内讨论极限。

Peano余项的Taylor展开，要求$f(x)$在$x=x_0$处n阶可导（只写前几项，懒得写第n项和Peano余项了）
$$
\begin{aligned}
f(x)&=f(x_0)+f'(x_0)(x-x_0)+\frac1{2!}f''(x_0)(x-x_0)^2+\dots+\frac1{n!}f^{(n)}(x_0)(x-x0)^n+o[(x-x_0)^n]\\
e^x&=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}\dots\\
\sin x&=x-\frac{x^3}6+\dots\\
\cos x&=1-\frac{x^2}{2!}+\dots\\
\ln(1+x)&=x-\frac{x^2}{2}+\frac{x^3}{3}+\dots\\
(1+x)^a&=1+ax+\frac{a(a-1)}{2!}x^2+\dots+\frac1{n!}a(a-1)(a-2)\dots(a-n+1)x^n+o(x^n)\\
\frac1{1-x}&=1+x+x^2+x^3+\dots\\
\frac1{1+x}&=1-x+x^2-x^3+\dots\\
\tan x&=x+\frac13x^3+\frac2{15}x^5+\dots\\
\arctan x&=x-\frac{x^3}3+\frac{x^5}5+\dots+\frac{(-1)^nx^{2n+1}}{2n+1}\\
\arcsin x&=x+\frac12\frac13x^3+\frac{1\times3}{2\times4}\frac15x^5+\dots=x+\frac{x^3} 6+\dots\\
\end{aligned}
$$

## 花里胡哨的求导

参数方程求导

隐函数求导

反函数求导

对数求导

高阶导

一阶微分形式不变性

## 中值定理

罗尔：

拉格朗日：

柯西：

## 应用

极值点和拐点以及凹凸性

渐近线

弧微分和曲率



