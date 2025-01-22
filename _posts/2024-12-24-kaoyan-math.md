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
- $e^{\infty}$型，包括$\lim\limits_{x\to0}e^{\frac1x},\lim\limits_{x\to\infty}e^{x}$，他们的极限都不存在（左右极限不相等）
- $\arctan\infty$型，包括$\lim\limits_{x\to0}\arctan\frac1x,\lim\limits_{x\to\infty}\arctan x$，极限不存在，左右极限不相等

证明极限存在的两个常用方法：夹逼法，一般是求n项和；单调有界，一般有递推式$x_{n+1}=f(x_n)$。还有什么传奇🐙老师的压缩映射，自行理解

其中，夹逼很经典的例子是：
$$
\lim\limits_{n\to\infty}\sqrt[n]{a_1^n+a_2^n+\dots+a_k^n}=max\{a_i\}
$$
单调有界数列必有极限。步骤：做差/商证单调，数学归纳法证有界，令极限为A，解方程。

压缩映射的核心是构建$ \vert x_{n+1}-A\vert \leq k^n\vert x_1-a\vert $的关系，通常使用导数或者拉格朗日中值定理

几个常用的极限：

| 1                                               | 2                                       | 3                                       |
| ----------------------------------------------- | --------------------------------------- | --------------------------------------- |
| $\lim\limits_{x\to0}\frac{1}{x}(a^{x}-1)=\ln a$ | $\lim\limits_{n\to\infty}\sqrt[n]{n}=1$ | $\lim\limits_{n\to\infty}\sqrt[n]{a}=1$ |
| $1^{\infty}=e^A$                                | 分式除法抓大头                          |                                         |

常用等价无穷小：懒得写，直接背泰勒

## 连续

函数在某点连续：在这个点的极限等于他的值。$\lim\limits_{x\to{x_0} }f(x)=f(x_0)$

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
- 介值定理：$\exists \xi\in(a,b),f(\xi)=C.\quad C\in[A,B]\subseteq[min,max] $
- 零点存在定理。注意是$f(a)f(b)<0$，当不严格小于0时，还要讨论等于0的情况。

# 一元导数，微分

## 定义

导数定义：$f'(x_0)=\lim\limits_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}=\lim\limits_{h\to 0}\frac{f(x_0+h)-f(x_0)}{h}$

微分：增量$\Delta y=f(x_0+\Delta x)-f(x_0)=A\Delta x+o(\Delta x)$，若A于$\Delta x$无关，则微分${\rm d}y=A\Delta x$，当$\Delta x$是一个小量时，$A=f'(x_0),{\rm d}y=f'(x_0)\Delta x=f'(x_0){\rm d}x$

一元函数的可微和可导是充要条件。可导一定有切线，有切线不一定可导。$f(x)=\sqrt x$

## 导数计算

常用导数：

$$
\begin{aligned}
(\arcsin x)'&=\frac1{\sqrt{1-x^2} }&(\arccos x)'&=-\frac1{\sqrt{1-x^2} }\\
(\arctan x)'&=\frac1{1+x^2}&({\rm arccot} x)'&=-\frac1{1+x^2}\\
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
\arctan x&=x-\frac{x^3}3+\frac{x^5}5+\dots+\frac{(-1)^nx^{2n+1} }{2n+1}\\
\arcsin x&=x+\frac12\frac13x^3+\frac{1\times3}{2\times4}\frac15x^5+\dots=x+\frac{x^3} 6+\dots\\
\end{aligned}
$$
泰勒展开解微分证明大题时，要注意展到几阶，在哪个点展开，对谁展开，余项的形式等问题

## 花里胡哨的求导

公式可能会看着很简单，但是记住不一定简单。还有但是，题做多了自然而然就会了

参数方程求导：$x=\varphi(t),y=\psi(t)$，则$\frac{ {\rm d}y}{ {\rm d}x}=\frac{ {\rm d}y}{ {\rm d}t}/\frac{ {\rm d}x}{ {\rm d}t}=\frac{\psi'(t)}{\varphi'(t)},\frac{ {\rm d}^2y}{ {\rm d}t^2}=\frac{ {\rm d} }{ {\rm d}t}\left(\frac{ {\rm d}y}{ {\rm d}x}\right)/\frac{ {\rm d}x}{ {\rm d}t}=\frac{ {\rm d} }{ {\rm d}t}\left(\frac{\psi'(t)}{\varphi'(t)}\right)\frac{1}{\varphi'(t)}$

隐函数求导：$F(x,y)=0$将$y$视作$x$的函数，两边分别对$x$求导，得到含$y'$的方程，解方程。或者，$\frac{ {\rm d}y}{ {\rm d}x}=-\frac{F_x'}{F_y'}$

反函数求导：$\frac{ {\rm d}y}{ {\rm d}x}=1/\frac{ {\rm d}x}{ {\rm d}y}$，互为反函数的导数互为倒数。

对数求导：多个因式乘除、根幂构成，两边同时取对数，之后再求导。常用于似然函数、复杂函数在某点的导数

高阶导：莱布尼茨$[u(x)v(x)]^{(n)}=\sum_{i=0}^{n}C_n^iu^{(n-i)}(x)v^{(i)}(x)$；$u,v$要么有高阶导的通项表达式($\ln x,\frac1{a+x}$)，要么求导后在这个点处为0（幂函数，代入为0）。计算高阶导还可以将函数拆分成多个能写出泰勒展开的多项式，通过泰特展开的唯一性得到高阶导的数值。

一阶微分形式不变性：复合函数的微分=外层函数微分x内层函数微分。

## 中值定理

罗尔：$[a,b]连续，(a,b)可导，f(a)=f(b),\exists\xi\in(a,b),f'(\xi)=0$

拉格朗日：$[a,b]连续，(a,b)可导，f(a)=f(b),\exists\xi\in(a,b),\frac{f(a)-f(b)}{a-b}=f'(\xi)$

柯西：$[a,b]连续，(a,b)可导，f(a)=f(b),g'(x)\neq0,\exists\xi\in(a,b),\frac{f(a)-f(b)}{g(a)-g(b)}=\frac{f'(\xi)}{g'(\xi)}$

零点个数：$f(x)$有$k$个零点，则$f'(x)$至少有$k-1$个零点；$f'(x)$有k个零点，则$f(x)$至多有$k+1$个零点。

## 应用以及一些其他的

- 极值：

必要条件：设$f(x)$在 $x=x_0$ 处可导,且在点 $x_0$ 处取得极值,则必有 $f'(x_0)=0$ .	

第一充分条件：设$ f(x)$ 在$x=x_0$处连续，且在$x_0$的某去心邻域$U(x_0,\delta)$ 内可导，左邻域和右邻域内，$f'(x)$符号不同，则极值存在。

第二充分条件：设$f(x)$在$x=x_0$处二阶可导,且$f'(x_0)=0,f''(x_0)\neq0$，若$f''(x_0)<0$,则$f(x)$在$x=x_0$处取得极大值

第三充分条件：设$f(x)$在$x_0$处$n$阶可导，且$f^{(m)}(x_0)=0,(m=1,2,\dots,n−1),f^{(n)}(x_0)\neq0(n\geq2)$ 且$n$为偶数，则极值存在。（区分极值点和拐点）

- 拐点与凹凸性：

同极值点。

$\forall x_1,x_2\in I$，凹：$f\left(\frac{x_1+x_2}{2}\right)<\frac{f(x_1)+f(x_2)}{2}$；凸$f\left(\frac{x_1+x_2}{2}\right)>\frac{f(x_1)+f(x_2)}{2}$

<img src="{{site.url}}/images/kaoyanmath/concavity.svg" alt="concavity" style="zoom:50%;" />

- 渐近线，考虑正负无穷

水平：$\lim\limits_{x\to\infty}f(x)=A$

垂直：$\lim\limits_{x\to x_0}f(x)=\infty$

斜：$\lim\limits_{x\to\infty}\frac{f(x)}{x}=a,\lim\limits_{x\to\infty}f(x)-ax=b$，则渐近线：$y=ax+b$

- 弧微分和曲率

弧微分${\rm d}s=\sqrt{1+y'^2}{\rm d}x$，曲率$k=\frac{\vert y''\vert }{(1+y'^2)^{3/2} }$，曲率半径$\rho=\frac1k$

曲率圆实际上是用圆去拟合函数，而切线就是用直线去拟合函数。都跟泰勒展开有点点关系。

- 但我们有条件$f''(x)>0$时，我们能想到那些东西？

  a $f(x),f'(x)$相关性质；b 拉格朗日余项缩放；c 凹凸性不等式；d $\int_a^bf(x){\mathrm d}x<\frac{f(a)+f(b)}2(b-a)$

- 对称性：关于点中心对称；关于直线对称；完全对称（多元函数任意两字母交换之后仍与原函数相同）；轮换对称。

- 常用的不等式

  - $ \vert a\vert =\vert a-b+b\vert \leq\vert a-b\vert +\vert b\vert $;$\vert a-b\vert =\vert a-c+c-b\vert \leq\vert a-c\vert +\vert c-b\vert $
  - $\frac2{(\frac1a+\frac1b)}\leq\sqrt{ab}\leq\frac{ab}2\leq\sqrt{\frac{a^2+b^2}2}$
  - $\frac{a^2}c+\frac{b^2}d\geq\frac{(a+b)^2}{c+d}$
  - Cauchy-Schwarz不等式: $(a_1b_1+a_2b_2)^2\leq(a_1^2+a_2^2)(b_1^2+b_2^2);\left[\int_a^bf(x)g(x){\mathrm d}x\right]^2\leq\int_a^bf^2(x){\mathrm d}x\int_a^bg^2(x){\mathrm d}x$
  - $\vert \int_a^bf(x){\mathrm d}x\vert\leq\int_a^b\vert f(x)\vert{\mathrm d}x$

