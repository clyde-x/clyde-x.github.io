---
layout: article
title: "飞行器动力学建模"
tags: "考研复试"
category: kaoyan
excerpt_separator: <!--brief-->
permalink: /kaoyan/aircraftDynamics
image:
  teaser: teaser1.jpg
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

# 动力学建模方法

## 动量定理

$\vec p=m\vec v,\frac{\mathrm d\vec p}{\mathrm dt}=\vec F$

刚体的动量定理：$\vec p=-\vec S\times\vec \omega+m\vec v_b$

刚体在本体系的静矩：$\vec S=\int_b(\vec r)_b\mathrm dm$，当本体系原点位于质心时，$S=0,\vec p=m\vec v_b$

## 动量矩定理

动量矩不仅与质点的动量有关，也与参考点的选取有关。要明确是相对哪一个点的动量矩。

<img src="{{site.url}}/images/kaoyanfushi/dljRef.png" alt="concavity" style="zoom:15%;" />

若取速度为$\vec v_s$的运动点$O_s$为参考点，则质点系相对于$O_s$的动量矩：$\vec H_s=\sum\vec r_{si}\times m_i\vec v_i$

对时间求导：$\frac{\mathrm d\vec H_s}{\mathrm dt}=\sum \frac{\mathrm d\vec r_{si}}{\mathrm dt}\times m_i\vec v_{i}+\vec r_{si}\times m_i\frac{\mathrm d\vec v_i}{\mathrm dt}$

由矢量关系$\vec r_{si}=\vec R_i-\vec R_s$，求导，得$\frac{\mathrm d\vec r_{si}}{\mathrm dt}=\vec v_i-\vec v_s,\frac{\mathrm d\vec r_{si}}{\mathrm dt}\times m_i\vec v_{i}=-\vec v_s\times m_i\vec v_i$

若记$\vec T_s=\sum \vec r_{si}\times \vec F_i$，作用于质点$p_i$的力对参考点$O_s$的力矩之和

则可以得到质点系的动量矩定理：$\frac{\mathrm d\vec H_s}{\mathrm dt}=\vec T_c-\vec v_s\times\vec P$

当参考点相对于惯性系静止即$\vec v_s=0$，或参考点为质心，即$\vec v_s\times\vec P=\vec v_s\times m\vec v_c=0$，简化为我们一般常见的
$$
\frac{\mathrm d\vec H_s}{\mathrm dt}=\vec T_s
$$
当受外力矩为0，则动量守恒。

**刚体**相对于本体系原点$O_b$的动量矩，在本体系中的分量列阵：
$$
(\vec H_b)_b=(I)_b(\vec\omega)_b+(\vec S)_b^\times(\vec v_b)_b
$$
其中$(I)_b=\int_b[(\vec r)_b^\times]^T(\vec r)_b^\times\mathrm dm$为刚体在本体系中的**惯性矩阵**，$(\vec S)_b$为上文提到的静矩

$$(I)_b=\begin{bmatrix}I_x&-I_{xy}&-I_{xz}\\-I_{xy}&I_y&-I_{yz}\\-I_{xz}&-I_{yz}&I_z\end{bmatrix}$$

主对角线上为主惯量$I_x=\int_b(y^2+z^2)\mathrm dm$，其余为惯量积$I_xy=\int_b(xy)\mathrm dm$

**动量矩定理**：$\frac{\mathrm d\vec H_b}{\mathrm dt}=\vec T_b+\vec v_b\times(\vec S\times\omega)$,若静矩为0，则$\frac{\mathrm d\vec H_b}{\mathrm dt}=\vec T_b=\sum\vec r_i\times \vec F_i$

# 平面大地飞行器运动方程

条件：速度不超过5马赫，大地是平面，不考虑曲率和旋转，大地是惯性参考系。

风速三角形：风速，大气的速度$V_w$；地速/航迹速度，质心相对于大地的速度$V_k$；空速/气流速度，质心相对大气的速度$V_a$

有$\vec V_k=\vec V_a+\vec V_w$

## 第一类坐标系（飞机）

|      | 大地坐标系$S_g$  | 本体坐标系$S_b$          | 气流坐标系$S_a$              | 航迹坐标系$S_k$                          |
| ---- | ---------------- | ------------------------ | ---------------------------- | ---------------------------------------- |
| 原点 | 地球表面某点     | 飞行器质心               | 质心                         | 质心                                     |
| x轴  | 水平面内任意方向 | 沿纵轴向前               | 沿气流速度矢量               | 沿航迹速度矢量                           |
| y轴  | 右手系           | 垂直对称面向右           | 右手系                       | 右手系                                   |
| z轴  | 铅锤向下         | 对称平面内垂直于纵轴向下 | 对称平面内垂直于气流速度向下 | 通过航迹速度矢量的铅锤平面内，垂直他向下 |

<img src="{{site.url}}/images/kaoyanfushi/ref1.png" style="zoom:50%;" />

- $\psi$偏航角，$\theta$俯仰角，$\varphi$滚转角。321旋转
- $\alpha$迎角/攻角，$\beta$侧滑角
- $\chi$航迹方位角， $\gamma$航迹倾斜角/爬升角

## 第二类坐标系（导弹）

|      | 地面坐标系$S_0$    | 弹体坐标系$S_1$       | 弹道坐标系$S_2$                   | 速度坐标系$S_3$         |
| ---- | ------------------ | --------------------- | --------------------------------- | ----------------------- |
| 原点 | 发射点             | 质心                  | 质心                              | 质心                    |
| x轴  | 弹道面与水平面交线 | 沿纵轴向前            | 沿速度矢量                        | 沿相对地面速度矢量      |
| y轴  | 铅锤向上           | 纵轴平面内与x垂直向上 | 通过速度矢量的铅锤平面内垂直x向上 | 纵向对称面内与x垂直向上 |
| z轴  | 右手系             | 右手                  | 右手系（类似航迹系）              | 右手系                  |

<img src="{{site.url}}/images/kaoyanfushi/ref2.png" style="zoom:60%;" />

- $\psi$偏航角，$\vartheta$俯仰角，$\gamma$滚转角。231旋转
- $\psi_v$弹道偏角，$\theta$弹道倾角，描述速度矢量相对于地面坐标系的方向
- $\alpha$迎角/攻角，$\beta$侧滑角，与第一组的攻角侧滑角在无风条件下定义相同
- $\gamma_v$速度倾斜角

## 空气动力

空气动力在速度系$S_3$中分解为阻力D，升力L，侧向力C，$(\vec R)_3=[-D,L,C]^T$（DLC名字特别好记）

每一个气动力都是$cqS$，c是阻力/升力/侧向力系数，S是特征面积，$q=\frac12\rho v^2$动压

- 阻力分为 零升阻力（摩擦压差波阻）和 诱导阻力（取决于升力），阻力与 马赫数、雷诺数、攻角、侧滑角 有关

- 升力系数与 零升力系数、攻角、升降舵偏角 有关

- 侧向力是由于空气不对称流过弹体纵轴对称面造成的（与升力形成原因相似），与 侧滑角、方向舵偏角 有关

## 动力矩，压力中心，焦点

**动力矩**分解为滚动力矩（副翼）、俯仰力矩（升降舵）、偏航力矩（方向舵），在弹体系1中描述

$M=mqSL$，m力矩系数，S特征面积，L特征长度

**压力中心**是气动作用力与纵轴交点，攻角不大时，把总升力的作用点近似为压力中心

**焦点**是由攻角引起的升力$c_y^\alpha qS\alpha$在纵轴上的作用点。

当升降舵偏角为$\delta_z$为0，且 零升系数$c_{y0}$为0时，压力中心与焦点重合

## 静稳定性

对于纵向、航向、横向，当$m_z^\alpha,m_y^\beta,m_x^\beta$小于0时稳定，大于0不稳定

## 质心运动方程

在弹道系$S_2$中描述**质心运动**：$m\frac{\mathrm d(\vec v)_2}{\mathrm dt}+(\vec\Omega)_2^\times(\vec v)_2=(\vec F)_2+(\vec P)_2$

其中$(\vec v)_2=[v,0,0,]^T;(\vec\Omega)_2=\vec{\dot\psi_v}+\vec{\dot\theta}=L_z(\theta)L_y(\psi_v)\cdot[0,\psi_v,0]^T+L_z(\theta)\cdot[0,0,\theta]^T$，（两次旋转从$S_0$到$S_2$）;推力$P$在弹体系，要转到弹道系；气动力$R$在速度系，要转到弹道系；重力$G$在地面系，转到弹道系。

在弹体系$S_1$中描述**绕质心运动**：$(I)_1\frac{\mathrm d(\vec \omega)_1}{\mathrm dt}+(\vec\omega)_1^\times(I)_1(\vec\omega)_1=(\vec M)_1$

其中$(I)$是惯性矩阵，$\omega$角速度，$M$主矩

$\omega=\vec{\dot \psi}+\vec{\dot \vartheta}+\vec{\dot \gamma}$，角度的处理方法同上

## 简化与分解

**侧向运动**：参数是$\beta,\gamma,\gamma_v,\omega_x,\omega_y,\psi,\psi_v,z$

**纵向运动**：参数是$v,\theta,\vartheta,\alpha,\omega_z,x,y$，只有质心在飞行平面内的运动，和绕弹体z轴的转动

纵向运动时，侧向运动参数全为0，导弹纵对称面与飞行铅锤面重合，地面坐标系x轴位于飞行平面内

纵向/侧向参数**解耦**：假设1侧向运动参数和舵偏角是小量，2弹道在铅锤面内，3，升降舵取决于纵向参量，方向舵副翼仅取决于侧向运动参量

## 机动性和过载

机动性：单位时间内改变飞行速度和大小的能力

过载表征机动性：$\vec n=\frac{\vec N}{G}$，即控制力和重力的比值，$N=P+R$

分析机动性，在$S_2$系；分析受力和结构，在$S_1$系

过载分为需用过载，极限过载（保持静稳定性，否则失速），可用过载（舵偏角最大时的法向过载）

用可用过载表示弹道系中的质心运动方程（两边同除重力）

$\frac{1}{g}\frac{dV}{dt}=n_{x2}-\sin\theta;\frac{V}{g}\frac{d\theta}{dt}=n_{y2}-\cos\theta-\frac{V}{g}\cos\theta;\frac{d\psi_{\nu}}{dt}=n_{z2}$

# 姿态运动学和动力学

姿态：航天器相对于空间某参考系的方位或者指向

姿态控制：施加力矩，保持/改变在空间的定向。按控制方式分为稳定和机动，是否消耗能源分为主动和被动

姿态确定：确定航天器的姿态，本体系相对于空间参考系。

姿态敏感器：方向敏感器（太阳、地球，星敏，磁强计，射频敏感器），惯性敏感器（陀螺仪加速度计）。太阳敏感器：太阳方向矢量与航天器特定轴的夹角；地球：对地平红外辐射探测，确定地平中心，获取当地垂线；星敏：测量恒星视线在航天器坐标系的方向矢量，得到相对于惯性系的姿态（双矢量）

执行机构分为推力器、角动量交换装置，磁力矩器。

喷气控制：不受外界影响；力矩大，三轴解耦；逻辑简单灵活；继电，非线性；相应快，机动能力强；适用于非周期大干扰力矩；适用于短寿命航天器（返回式卫星）

## 单刚体航天器姿态动力学与运动学

**常用坐标系以及姿态角**

|      | 惯性系$S_i$                        | 第二轨道坐标系$S_o'$或$S_o$    | 本体系$S_b$  |
| ---- | ---------------------------------- | ------------------------------ | ------------ |
| 原点 |                                    | 质心                           | 质心         |
| x    |                                    | 轨道平面内，垂直于z指向前      | 前，惯性主轴 |
| y    | 垂直于轨道平面，与$\vec H$方向相反 | 垂直轨道平面与$\vec H$方向相反 | 右，惯性主轴 |
| z    |                                    | 指向地心                       | 下，惯性主轴 |

**姿态角**：航天器本体坐标系相对于第二轨道坐标系的欧拉角，用滚转角$\varphi$，俯仰角$\theta$，偏航角$\psi$,描述。

第一套欧拉角321旋转，无法描述自旋卫星的姿态；第二套312旋转

**运动方程**：$\omega=\omega_r+\omega_{orb}$，绝对角速度=本体系相对轨道角速度+牵连角速度（轨道系的绝对角速度）。把方程放到本体系

在轨道系中， $ (\omega_{orb})_{o}=[0,-\Omega,0]^T$ ,其中 $\Omega$ 是轨道角速率。

坐标变换，通过 $L_{bo}$ 转到本体系上，最后会得到 $\omega$ 的三分量的表达式。两套欧拉角不同

**动力学方程**

$\frac{\mathrm d(\vec H)_b}{\mathrm dt}+(\omega)_b^\times(\vec H)_b=(\vec M)_b,\vec H=I\omega$即$(I)_b\frac{\mathrm d(\vec \omega)_b}{\mathrm dt}+(\omega)_b^\times(I)_b(\vec \omega)_b=(\vec M)_b$

$(I)_b$ 为惯性矩阵，当本体系为惯性主轴系，惯量积为0，只有主惯性矩

## 带角动量交换装置的刚体

角动量交换装置：某种控制执行机构，工作原理是角动量守恒。$H_b+H_w=C$，通过改变角动量交换装置的角动量，来控制飞行器的角动量。分类有

- 反作用飞轮，也叫零动量飞轮，标称转速为0，仅在轴向提供控制力矩，航天器姿态稳定时总角动量为0
- 偏置飞轮，也叫动量飞轮，标称转速不为0，具有陀螺定轴性
- 单/双框架控制力矩陀螺，改变转子角动量方向从而输出控制力矩。转子恒定高速转动，框架根据指令低速转动。具有力矩放大的效果，适用于大型长寿命航天器和快速机动的航天器

$H=H_b+\sum H_i$，本体的角动量+每个转子相对于质心的角动量.

### 飞轮

$$
(H)_b=(I_o)(\omega)_b+\sum (H_{wi})_b
$$

将各个飞轮视为质点时的惯量矩阵x整体角速度+飞轮i对其自身质心的绝对角动量

飞轮i对其自身质心的绝对角动量，一般只考虑轴向的角动量，即 $(H_{wi})=c_{wi}I_{wi}\left(\Omega_i+c_{wi}^T(\omega)_b\right)$

其中 $c_{wi}$为飞轮i在本体系中的方向余弦矩阵，$\Omega$ 时飞轮i相对卫星本体的转速， $I_{wi}$ 是飞轮i的轴向转动惯量

对上式求和，$\sum (H_{wi})_b=CI_w\Omega+CI_wC^T(\omega)_b，C\in \mathbb R^{3\times n},I\in \mathbb R^{n\times n},R\in\mathbb R^{n\times1}$

则 $(H)_b=(I_t)_b(\omega)_b+CI_w\Omega$ ，其中 $(I_t)_b=(I_o)_b+CI_wC^T$ 是飞轮组锁定时的整体惯量矩阵，另一项是飞轮组相对于星体的三轴角动量

动量矩定理：$\frac{\mathrm dH}{\mathrm dt}+\omega_b^\times H= I_t \frac{\mathrm d\omega_b}{\mathrm dt}+\omega_b^\times(I_t\omega_b+CI_w\Omega)=T_w+T_d$，其中$T_w=-CI_w\dot \Omega $ 是飞轮的控制力矩，包含角速度的变化$\dot \Omega$，是飞轮的输出量

### 飞轮的性能

飞轮的安装有三正交、三正交+一斜装，四斜装。

性能指标有冗余度（允许任意失效的最大个数），可靠度（1-整体失效的海旅），功耗（定义为各个飞轮输出力矩的平方和 $T_n^TT_n$，功耗控制是一个等式约束的最优化问题，要求飞轮组在三轴的输出力矩=需要的控制力矩），角动量可调节性（转速，安装角）等

操纵率的求解，就是飞轮力矩方程的逆求解 $T_c=-C_w\dot\Omega$ ，已知指令力矩 $T_c=T_w$ ，和等效安装矩阵 $C_w$，求解 $\dot \Omega$。满秩时直接求逆求解，非满秩时设计**能耗最小操纵率**/**轮速平衡操纵率**最优求解

## 空间干扰力矩

- 气动力矩，大气分子撞击航天器表面进行动量交换
- 地磁力矩，航天器的偶极子磁矩于地磁场作用
- 太阳光压力矩，太阳光量子。有反射（漫反射镜面反射），吸收（完全吸收），透射
- 引力梯度力矩，各部分质量不同。与姿态角有关，若任意一个惯性主轴是铅锤的，引力梯度力矩为0。还能推导出引力梯度稳定的条件，懒得写了。

# 轨道动力学

## 轨道平面内的Kepler轨道力学

**引力**：$m\vec g=-\frac{GmM}{r^3}\vec r$，地球引力常数$GM=\mu$

**动量矩**：$\vec H=\vec r\times \vec v=const$，动量矩是常量，垂直于轨道平面

**能量**：$E=\frac12v^2-\frac\mu r=const$，能量=动能+势能是常量

**拉普拉斯矢量**：$\vec L=\vec v\times \vec H-\mu(\frac{\vec r} r)=const$，Laplace矢量是常量

关系：$\vec L与\vec H$垂直，大小关系$L^2=\mu^2+2EH^2$

**轨道方程**：$\vec L\cdot \vec r=H^2-\mu r$

$r=\frac{p}{1+e\cos\theta}$，其中$p=\frac{H^2}\mu,e=\frac L\mu,a=\frac p{1-e^2},r_p=\frac{p}{1+e},r_a=\frac p{1-e}$，半通径，偏心率，半长轴，近地点，远地点

能量是常量，对于椭圆轨道，$e<1,E=-\frac \mu{2a}$，**轨道能量取决于半长轴a**

**轨道速度**分解为**径向**$v_r=\sqrt{\frac\mu p}e\sin\theta$和**横向**$v_u=\sqrt{\frac\mu p}(1+e\cos \theta)$；圆轨$v=v_u=\sqrt{\frac\mu p}$

**时间，角度**：偏近点角E与真近点角$\theta$：$1+e\cos\theta=\frac{1-e^2}{1-e\cos E},\tan\frac\theta2=\sqrt{\frac{1+e}{1-e}}\tan\frac E2$

<img src="{{site.url}}/images/kaoyanfushi/EandTheta.png" style="zoom: 33%;" />

图中，O是地球，P是近地点，C是椭圆轨道中心，椭圆是真实轨道，圆轨道是想象的。

平近点角M：假设以平均角速度$\sqrt\frac\mu{a^3}$运行时间t后的角度，不真实存在：$M=\sqrt\frac\mu{a^3}(t-t_p)$

有开普勒方程：$M=E-e\sin E$，迭代数值求解

## 轨道要素

- 升/降交点：航天器轨道与赤道面的交点，升：南-北，降：北-南
- 交点线/节线：升降交点的连线OB，也是航天器轨平面与赤道平面的交线
- **升交点赤经$\Omega$**：赤道惯性系的ox轴与交点线DB之间的角度，自西向东，0~360
- **轨道倾角$i$**：轨道面与赤道面的夹角，也是地球自转轴与轨道发现的夹角。0~180，<90，偏东，顺行；>90，偏西，逆行；=90极轨道
- **近地点幅角$\omega$**：拱点线OP（椭圆中心与近地点连线）与交点线OB的角度，0~360
- **时间基准$t_p$**：规定航天器经过近地点时为基准时间

六个轨道要素：

- $a,e$决定轨道形状大小
- $\Omega,i$决定轨道平面取向
- $\omega$决定拱点线在轨道平面位置
- $t_p$时间基准

特殊的，

- $i=0/180$，升交点、交点线、近地点幅角不定但$\alpha_p=\Omega+\omega$近地点赤经确定
- $e=0$，近地点不定，近地点幅角，时间基准不定，可以用升交点代替近地点
- $i=0/180,e=0$，赤道面内的圆轨道，$a=r$，时间基准选为通过春分点的时刻

