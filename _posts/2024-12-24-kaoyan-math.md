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

- 常用的不等式（随便看看得了）

  - $ \vert a\vert =\vert a-b+b\vert \leq\vert a-b\vert +\vert b\vert $;$\vert a-b\vert =\vert a-c+c-b\vert \leq\vert a-c\vert +\vert c-b\vert $
  - $\frac2{(\frac1a+\frac1b)}\leq\sqrt{ab}\leq\frac{ab}2\leq\sqrt{\frac{a^2+b^2}2}$
  - $\frac{a^2}c+\frac{b^2}d\geq\frac{(a+b)^2}{c+d}$
  - Cauchy-Schwarz不等式: $(a_1b_1+a_2b_2)^2\leq(a_1^2+a_2^2)(b_1^2+b_2^2);\left[\int_a^bf(x)g(x){\mathrm d}x\right]^2\leq\int_a^bf^2(x){\mathrm d}x\int_a^bg^2(x){\mathrm d}x$
  - $\vert \int_a^bf(x){\mathrm d}x\vert\leq\int_a^b\vert f(x)\vert{\mathrm d}x$

# 一元积分学

## 定积分

定积分存在：被积函数在**闭**区间内有有限个间断点。$\int_a^bf(x){\mathrm d}x=\lim\limits_{\lambda\to0}\sum_{i=1}^{n}f(\xi_i)\Delta x_i$

用定积分求极限，先提出一个$\frac1n$，剩下的就是被积函数，把变化的部分用含$i$的式子替换，即$x=\frac in$，然后再注意积分的上下限（一般是01）。2021年数一的一道选择题就很经典，能加深对定积分和求和之间关系的理解。

## 不定积分技巧

### 常用积分

但是不太好记的，记不住也没关系，熟悉他们的推导过程，也能举一反三。
$$
\begin{aligned}
&\int\tan x{\mathrm d}x=\int\frac{\sin x}{\cos x}{\mathrm d}x=-\ln \vert\cos x\vert+C\\
&\int\cot x{\mathrm d}x=-\ln\vert\sin \vert+C\\
&\int\frac1{\cos x}{\mathrm d}x=\frac12\ln\frac{1+\sin x}{1-\sin x}+C=\ln\vert\tan x+\frac1{\cos x}\vert+C\\
&\int\frac1{\sin x}{\mathrm d}x=\frac12\ln\frac{1-\cos x}{1+\cos x}+C=\ln\vert\csc x-\cot x\vert+C\\
&\int\frac1{\cos^2x}{\mathrm d}x=\tan x+C\\
&\int\frac1{\sin^2x}{\mathrm d}x=-\cot x+C\\
&\int\frac1{a^2+x^2}{\mathrm d}x=\frac1a\arctan\frac xa+C\\
&\int\frac1{a^2-x^2}{\mathrm d}x=\frac1{2a}\ln\vert\frac {a+x}{a-x}\vert+C\\
&\int\frac1{\sqrt{a^2-x^2}}{\mathrm d}x=\arcsin \frac ax+C\\
&\int\frac1{\sqrt{x^2-a^2}}{\mathrm d}x=\ln\vert x+\sqrt{x^2-a^2}\vert+C\\
&\int\frac1{\sqrt{x^2+a^2}}{\mathrm d}x=\ln\vert x+\sqrt{x^2+a^2}\vert+C\\
\end{aligned}
$$

### 常用换元

三角换元：把$x$换成$t$

$\sqrt{a^2-x^2},x=a\sin t;\quad\sqrt{x^2+a^2},x=a\tan t\quad\sqrt{x^2-a^2},x=a\sec t$

<img src="{{site.url}}/images/kaoyanmath/sanjiaohuanyuan.jpg" alt="concavity" style="zoom:50%;" />

还可以使用**万能公式**、**齐次化**等技巧对含三角函数的被积函数进行换元

被积函数$R(x,(ax+b)^{\frac1n},(ax+b)^{\frac1m})$，令$(ax+b)^{\frac1{mn}}=t$

被积函数含复杂根式，将整个根式令为t

### 分部积分

$$
\int u{\mathrm d}v=uv-\int v{\mathrm d}u
$$

u一般是函数本身复杂，导数简单的，如$\ln x,\arctan x,\arcsin x$

v一般是函数原函数和导数差不多的，如$e^x,\sin x,\cos x$

对于$\int e^x\sin x{\mathrm d}x,\int e^x\cos x{\mathrm d}x$连用两次分部积分，然后解方程

### 有理分式

把分式化为最简，$R(x)=\frac{P(x)}{Q(x)}$，分子次数小于分母次数

把有理分式分解为简单分式的和：$\frac{A}{x-a},\frac{Mx+N}{x^2+px+q},\frac{B_i}{(x-b)^i}$，可以用留数法解各个的系数

### 其他的（华理士之类的）

$$\int_0^{\frac\pi2}\sin^nx{\mathrm d}x=\int_0^{\frac\pi2}\cos^nx{\mathrm d}x=\begin{cases}&\frac{n-1}{n}\frac{n-3}{n-2}\cdots\frac12\frac\pi2,n为偶数\\&\frac{n-1}{n}\frac{n-3}{n-2}\cdots\frac23,n为奇数\end{cases}$$

区间换到$\pi$或者$2\pi$之类的自己再推推

$\int_0^\pi xf(\sin x){\mathrm d}x=\frac\pi2\int_0^\pi f(\sin x){\mathrm d}x$

## 积分中值定理

$f(X),g(X)$在$[a,b]$连续，且$g(x)$不变号，则$\exists \theta\in[a,b],{\mathrm {s.t.}}\int_a^bf(x)g(x)\mathrm dx=f(\theta)\int_a^bg(x)\mathrm dx$

以上为积分第二中值定理，当$g(x)=1$时，退化为积分第一中值定理

## 反常积分

无界函数的奇点与“这个点分母是否为0”没有关系，例如$\int_0^1\ln x \mathrm dx,\int_0^1\frac1{x^2}e^{-\frac1x}\mathrm dx$，$x=0$，是前者的奇点，不是后者的奇点。

反常积分是否收敛，与函数极限为0，没有关系。[这篇文章](https://zhuanlan.zhihu.com/p/342471635)有具体的例子。

### 审敛

- 无界p积分：$\int_1^{+\infty}\frac1{x^p}\mathrm dx=\frac{\infty^{1-p}-1}{1-p},p>1收敛,p\leq1发散$

- 瑕p积分：$\int_0^1\frac1{x^p}\mathrm dx=\frac{1-0^{1-p}}{1-p},p<1收敛,p\geq1发散$

- 绝对收敛必收敛

- 比较判别法的极限形式：$\lim\limits_{x\to\infty}\frac{f(x)}{\varphi(s)}=l$，$0<l<\infty$两个函数同敛散；$l=0$分子收敛则分母收敛；$l=\infty$分子发散则分母发散

- Cauchy判别法：取$\varphi(x)=\frac1{x^p}$，即$\lim\limits_{x\to\infty}x^pf(x)=l$，$0\leq l<\infty,p>1$收敛；$0<l\leq \infty,p\leq1$发散

- 瑕积分的Cauchy判别：$\lim\limits_{x\to b}(x-b)^pf(x)=l$，$0\leq l<\infty,p<1$收敛；$0<l\leq \infty,p\geq1$发散

- 万能公式（其中瑕积分仅指$x\to0$的时候，当$x\to1$时把$\ln x$当成$x-1$，再换元）

  $\int\frac{1}{x^\alpha\ln^\beta x}\mathrm dx$，瑕积分：$\alpha<1或\alpha=1,\beta>1$收敛；无穷积分：$\alpha>1或\alpha=1,\beta>1$收敛

- 当奇偶函数单边不收敛时，不能使用对称性消掉

- 超纲，Abel，Direchlet

## 定积分的应用

面积$S=\int_a^b[y_2(x)-y_1(x)]\mathrm dx=\frac12\int_\alpha^\beta r^2(\theta)\mathrm d\theta=\int_\alpha^\beta\vert y(t)x'(t)\vert\mathrm dt$

旋转体体积$V=\pi\int_a^by^2(x)\mathrm dx$（绕x轴）

弧长$s=\int_\alpha^\beta\sqrt{x'^2(t)+y'^2(t)}\mathrm dt=\int_a^b\sqrt{1+y'^2(x)}\mathrm dx=\int_\alpha^\beta\sqrt{ r^2(\theta)+r'^2(\theta)}\mathrm d\theta$

旋转曲面面积$S=2\pi\int_a^b\vert y\vert\sqrt{1+f'^2(x)}\mathrm dx=2\pi\int_\alpha^\beta\vert y(t)\vert\sqrt{x'^2(t)+y'^2(t)}\mathrm dt=2\pi\int_\alpha^\beta r(\theta)\sqrt{r^2(\theta)+r'^2(\theta)}\mathrm d\theta$

## 区间再现

定积分上下限不变的换元，多用于三角函数参杂在指对幂函数中，且区间含有$\pi$（没啥用）
$$
\int_a^bf(x)dx=\int_a^bf(a+b-x)dx,令u=a+b-x\\
\int_a^bf(x)dx=\frac12\int_a^bf(x)+f(a+b-x)dx,被积函数满足f(x)+f(a+b-x)简单
$$

## 用留数分解分式 

在复变函数、自动控制中比较常用，对于复杂分式的分解
$$
\frac{P(x)}{Q(x)}=\frac{C_1}{(x-z)^n}+\frac{C_2}{(x-z)^{n-1}}+\cdots\\
C_k=\lim_{x\to z}\frac1{(k-1)!}\frac{d^{k-1}}{dx^{k-1}}[\frac PQ(x-z)^n]
$$
例如$\dfrac{x^3+2x^2+1}{x^4+6x^3+14x^2+8}$
$$
f(x)=\frac A{(x+2)^2}+\frac B{x+2}+\frac{ax+b}{x^2+2x+2}\\
A=\lim_{x\to2}\frac{x^3+2x^2+1}{x^2+2x+2}=\frac12,B=\lim_{x\to2}[\frac{x^3+2x^2+1}{x^2+2x+2}]'=\frac52,ab可以待定系数
$$

# 多元函数微分学

## 概念

重极限：邻域中的点无论以任何方式趋近$P_0(x_0,y_0)$时，函数都趋近于同一常数A

偏导：$f_x'(x_0,y_0)=\frac{\partial f(x,y)}{\partial x}|_{(x_0,y_0)}=\lim_{\Delta x\to 0}\frac{f(x_0+\Delta x,y_0)-f(x_0,y_0)}{\Delta x}$实际上是一元函数的导数。几何上表示曲面与平面$y=y_0$的交线在$x_0$处的斜率

全增量：$\Delta z = f(x+\Delta x,y+\Delta y)-f(x,y)=A\Delta x+B\Delta y+o(\sqrt{(\Delta x)^2+(\Delta y)^2})$则$dz=A\Delta x+B\Delta$为全微分

可微$\to$连续，偏导存在，且$dz=\frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy$

偏导连续$\to$可微，

可导：两个偏导数都存在。可导既不可以推连续（由重极限定义），也不可以推可微

方向导数：l为$(x_0,y_0)$出发射线，$(x,y)$为射线上一点，$\rho$为两点间距离，则
$$
\frac{\partial f}{\partial l}|_{(x_0,y_0)}=\lim_{\rho\to0^+}\frac{f(x,y)-f(x_0,y_0)}{\rho}=\frac{\partial f}{\partial x}\cos\theta+\frac{\partial f}{\partial y}\sin\theta
=\nabla f\cdot\vec{e}
$$
在所有方向导数中，沿着$\nabla$的最大，为$\nabla$的模长。

判断可微：求在点处的两个偏导（用定义，极限求）；判断师是否趋于0，
$$
\lim_{\Delta x,\Delta y\to0}\frac{f(x_0+\Delta x,y_0+\Delta y)-f(x_0,y_0)-\frac{\partial f}{\partial x}\Delta x-\frac{\partial f}{\partial y}\Delta y}{\sqrt{(\Delta x)^2+(\Delta y)^2}}=0
$$
若函数的混合二阶偏导数连续，则相等

隐函数：$\dfrac{\partial y}{\partial x}=-\dfrac{F_x}{F_y}$，$F(x,y)=0$，$F_x,F_y$分别为$x,y$的偏导数，$\dfrac{\partial z}{\partial x}=-\dfrac{F_x}{F_z},\dfrac{\partial z}{\partial y}=-\dfrac{F_y}{F_z}$

由方程组$F(x,u,v)=0,G(x,u,v)=0$，则$F_x'+F_u'\frac{\partial u}{\partial x}+F_v'\frac{\partial v}{\partial x}=0$，$G_x'+G_u'\frac{\partial u}{\partial x}+G_v'\frac{\partial v}{\partial x}=0$，联立方程组求解$\frac{\partial u}{\partial x},\frac{\partial v}{\partial x}$

## 多元极值

充分条件：$f_x'=0,f_y'=0$，$f_{xx}''=A,f_{yy}''=B'',f_{xy}''=f_{yx}''=C$，则$AC-B^2>0$，取极值，$A>0$极小值，$A<0$极大值；$AC-B^2=0$不确定；$AC-B^2<0$不取极值。

步骤：求驻点（包含偏导不存在的点），求ABC判别。

条件极值：Lagrange乘数法，$f(x,y)$在条件$\phi(x,y)=0$下的极值：$F(x,y,\lambda)=f(x,y)+\lambda\phi(x,y)$，求偏导数，$F_x'=0,F_y'=0,F_\lambda'=0$，求解方程组
$\lambda$为拉格朗日乘数，$\lambda=\frac{\partial f}{\partial \phi}$，$\lambda$的几何意义是切平面与约束曲面的法向量的夹角

均值不等式：调和，几何，算数，平方$\dfrac{n}{\dfrac1x_1+\frac1x_2+\cdots+\dfrac1{x_n}}\leq \sqrt[n]{x_1x_2\cdots x_n}\leq\dfrac{x_1+x_2+\cdots+x_n}{n}\leq\sqrt{\dfrac{x_1^2+x_2^2+\cdots+x_n^2}n}$

多元泰勒：
$$
f(\vec x)=f(\vec x_0)+\nabla f(\vec x_0)^T\cdot(\vec x-\vec x_0)+\frac1{2!}(\vec x-\vec x_0)^T\nabla^2 f(\vec x_0)(\vec x-\vec x_0)+o(\|\vec x-\vec x_0\|^2)
$$

二元泰勒：
$$
f(x,y)=f(x_0,y_0)+\frac{\partial f}{\partial x}(x-x_0)+\frac{\partial f}{\partial y}(y-y_0)+\frac{1}{2!}\left[\frac{\partial^2 f}{\partial x^2}(x-x_0)^2+2\frac{\partial^2 f}{\partial x \partial y}(x-x_0)(y-y_0)+\frac{\partial^2 f}{\partial y^2}(y-y_0)^2\right]+o(\Delta x^2+\Delta y^2)\\   =
f(x_0,y_0)+[f_x'(x_0,y_0),f_y'(x_0,y_0)]\begin{bmatrix}x-x_0\\ y-y_o\end{bmatrix}+\frac12\begin{bmatrix}x-x_0&y-y_0\end{bmatrix}\begin{bmatrix}f_{xx}''&f_{xy}''\\ f_{yx}''&f_{yy}''\end{bmatrix}\begin{bmatrix}x-x_0\\ y-y_o\end{bmatrix}+o(\Delta x^2+\Delta y^2)
$$

