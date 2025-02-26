---
layout: article
title: "飞行器动力学建模"
tags: "考研复试"
category: kaoyan
excerpt_separator: <!--brief-->
permalink: /kaoyan/aircraftDynamics
---
复习一下飞行器动力学建模，这是大二由贾老师和金老师教授的课程，是我们后面轨道动力学，以及进行控制的基础。要熟练掌握各种坐标系变换，动力学特征等内容。
<!--brief-->
# 矢量运算与坐标变换

## 矢量和矢阵

在一个坐标系下$S_a$，矢量可以写为 分量列阵与矢阵的数量积，(两者都是三维列向量)，即

$$
\vec u=[u_{xa},u_{ya},u_{za}][\vec i_a,\vec j_a,\vec k_a]^T=(\vec u)_a^T\cdot f_a
$$

前者 $ (\vec u)_a$ 为分量列阵，由矢量 $\vec u$ 在坐标系 $S_a$ 下的各个分量组成的

后者 $f_a=[\vec i_a,\vec j_a,\vec k_a]^T$ 为矢阵，为单位矢量矩阵，本质是一个矩阵，即 $\vec i_a=[1,0,0]^T,\vec j_a=[0,1,0]^T,\vec k_a=[0,0,1]^T$

矢量与参考系无关，分量列阵与参考系有关

## 矢量运算的坐标表示

$$
\begin{aligned}
&\vec u\cdot\vec v=(\vec u)_a^T(\vec v)_a\\
&\vec u\times\vec v=f_a^T(\vec u)_a^\times (\vec v)_a\\
&(\vec u\times\vec v)_a=(\vec u)_a^\times (\vec v)_a\\
&其中(\vec u)_a^\times=\begin{bmatrix}0&-u_z&u_y\\u_z&0&-u_x\\-u_y&u_x&0\end{bmatrix}为叉乘反对称阵
\end{aligned}
$$

## 坐标变换

从$S_a$到$S_b$的坐标变换矩阵：$L_{ba}=f_b\cdot f_a^T$，一个坐标的单位矢量在另一个坐标系的分量列阵

$(\vec u)_b=L_{ba}(\vec u)_a$

## 基元旋转矩阵

基元旋转矩阵有正交性，传递性，行列式为1等性质
$$
L_x(\alpha)=\begin{bmatrix}1&0&0\\0&\cos\alpha&\sin\alpha\\0&-\sin\alpha&\cos\alpha\end{bmatrix}L_y(\beta)=\begin{bmatrix}\cos\beta&0&-\sin\beta\\0&1&0\\\sin\beta&0&\cos\beta\end{bmatrix}L_z(\gamma)=\begin{bmatrix}\cos\gamma&\sin\gamma&0\\-\sin\gamma&\cos\gamma&0\\0&0&1\end{bmatrix}
$$
$L_x(\alpha)$即绕x轴旋转$\alpha$角度

记忆方法：记住1的位置，1所在的行列除它外全为0；然后$-\sin$在1的右上方，几个三角函数形成十字交叉

**注意**：在MATLAB中的旋转矩阵定义与此稍有不同，编程的时候记得看一下

相继三次转动$R_z(\psi)\to R_y(\theta)\to R_x(\varphi)$，实现从a系到b系的坐标变换：$L_{ba}=L_x(\varphi)L_y(\theta)L_z(\psi)$

欧拉角的旋转总共有12种

### 由两个矢量的分量列阵求坐标变换矩阵

由两个矢量的分量列阵求坐标变换矩阵$L_{ba}$，已知$\vec p,\vec q$在$S_a,S_b$种的分量列阵，求$L_{ba}$

定义新坐标系$S_c$，$\vec i_c$指向$\vec p$，$\vec k_c$指向$\vec p\times\vec q$，$\vec j_c$右手系
$$
(\vec i_c)_a=\frac{(\vec p)_a}{p},(\vec k_c)_a=\frac{(\vec p)_a^\times(\vec q)_a}{\vert\vert\vec p\times\vec q\vert\vert},(\vec j_c)_a=(\vec k_c)_a^\times(\vec i_c)_a\\
L_{ca}=[(\vec i_c)_a^T,(\vec j_c)_a^T,(\vec k_c)_a^T]^T\\
同理可得L_{cb}=[(\vec i_c)_b^T,(\vec j_c)_b^T,(\vec k_c)_b^T]^T\\
L_{ba}=L_{bc}L_{ca}=L_{cb}^TL_{ca}
$$
航天器的双矢量定姿就是这个原理

### 非惯性系矢量求导

$绝对导数=相对倒数+\vec\omega\times\vec u，\frac{\mathrm d\vec u}{\mathrm dt}=\frac{\mathrm d_a\vec u}{\mathrm dt}+\vec{\omega_a}\times\vec u$

分量列阵形式：$(\frac{\mathrm d\vec u}{\mathrm dt})_a=\frac{\mathrm d(\vec u)_a}{\mathrm dt}+(\vec{\omega_a})_a^\times\vec u$

其中$(\frac{\mathrm d\vec u}{\mathrm dt})_a$是$\vec u$对时间相对导数的列阵，$\frac{\mathrm d(\vec u)_a}{\mathrm dt}$是$\vec u$在坐标系$S_a$中分量列阵的导数。

二阶导数：（第二个等号是假设角速度$\omega_a$为常值）

$$
\begin{aligned}
\frac{\mathrm{d}^2\vec{u}}{\mathrm{d}t^2}
&= f_{a}^{\mathrm{T}} \frac{\mathrm{d}^2 (\vec{u})_a}{\mathrm{d}t^2} + 2f_{a}^{\mathrm{T}} (\bar{\omega}_a)_a^{\times} \frac{\mathrm{d} (\vec{u})_a}{\mathrm{d}t} + f_{a}^{\mathrm{T}} (\bar{\boldsymbol{\omega}}_a)_a^{\times} (\bar{\boldsymbol{\omega}}_a)_a^{\times} (\bar{u})_a \\
&= \frac{\mathrm{d}_a^2 \vec{u}}{\mathrm{d}t^2} + 2\vec{\omega}_a \times \frac{\mathrm{d}_a \vec{u}}{\mathrm{d}t} + \vec{\omega}_a \times (\vec{\omega}_a \times \vec{u})
\end{aligned}
$$


坐标变化矩阵的变化率：
$$ \dot L_{bi} = -(\vec{\omega}_b)_b^\times L_{bi} $$