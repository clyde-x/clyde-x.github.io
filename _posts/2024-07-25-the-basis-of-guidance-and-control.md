---
layout: article
title: 制导与控制基础
tags: "BUAA课内"
category: BUAA_course
excerpt_separator: <!--brief-->
permalink: /BUAA/first
---
这是大三春季学期开设的一门课，我学的极其痛苦，其中涉及很多公式和概念，需要熟练掌握数学和力学。为了应付期末考试，我边复习边写下了这个文档，作为知识点的总结。事实证明，在了解制导控制的重要概念和思想之后，再背一下计算题（不是），期末考试基本上能得心应手，除了好几道大题没复习到，最后计算题没算完。
<!--brief-->
{% include toc.html %}

# 开环制导

——大气层内上升段飞行程序设计（飞行程序是一个离线设计的指令序列）

闭环制导：采用实时状态信息，校正制导目标与预测目标的偏差，实时计算制导指令

大气层内开环制导的关键：设计飞行程序

![开环制导和闭环制导]({{site.url}}/images/img_0726/img/001.png)

# 火箭运动方程

## 坐标系

### 定义

- 发射坐标系l  发射点，发射方向，垂直发射水平面向上，右手
- 本体坐标系b  质心，沿纵轴，主对称面内垂直x轴向上，右
- 速度坐标系a  质心，速度，主对称面内垂直x轴，右

### 转化

- 速度a--弹体b  侧滑角$y-\beta$,攻角$z-\alpha$
- 发射l-速度a  321速度倾斜角$z-\theta$，航迹偏航角$y-\sigma$，倾侧角$x-\nu$

## 火箭上的力

- 推力
- 气动力DLC
- 引力

## 质心动力学方程和运动学方程

## 绕质心的运动学和动力学方程

## 运动学方程简化

### 基本假设

- 引力假设：引力只沿$y_l$轴方向，服从平方反比
- 地球自转假设：忽略地球自转，没有哥氏加速度和牵连加速度$\omega_E==0$
- 小角度假设：欧拉角（攻角，侧滑角，偏航角，滚转角，航迹偏航角，倾侧角，速度倾斜角-俯仰角），以及发动机摆角控制量为小量。还有$\alpha=\varphi-\theta$
- 力矩瞬时平衡假设：研究质心运动时不考虑动态过程。俯仰：$\delta_\varphi=-\frac{M_{z1}^\alpha}{M_{z1}^\delta}\alpha$即在俯仰通道，由发动机俯仰角带来的俯仰推力力矩和由攻角带来的俯仰气动力矩平衡；在偏航通道，则是$\delta_\psi$和$\beta$

### 质心运动方程的简化

### 攻角和程序姿态角

需要攻角随时间的变化规律，即**飞行程序**，飞行程序设计-->攻角飞行程序设计

利用力矩瞬时平衡建立**攻角**和**程序姿态角**的关系：

$\delta_\varphi=a_0^\varphi(\varphi-\varphi_{pr})$，小角度简化，$\alpha=A(\varphi_{pr}-\theta)$

# 火箭运动特性

纵向运动=切向运动+法向运动

## 切向

分析$\dot{v}$和$F_p$

齐奥尔科夫斯基火箭方程，提高速度，提高燃料利用率

## 法向

决定v的方向，火箭转弯（垂直上升段，**转弯段**，瞄准段）

分析$\dot{\theta}$，垂直上升段$\theta=\varphi=0$不转弯；转弯段，靠攻角（推力+气动力）启动转弯过程

--> 程序姿态角$\varphi_{pr}$设计小于90度，发动机偏转，产生$\delta_\varphi$由力矩平衡，得到攻角角度$\alpha$（先由$\varphi_{pr}$得到$\delta_{\varphi}$再产生攻角）

## 静稳定性

重心位于压心之前，静稳定

静稳定火箭的转弯过程：程序轴、弹轴、速度轴，相应的力和力矩的方向、平衡。

体轴一直在指令轴和速度轴之间
$$
\varphi-\varphi_{pr}>0\quad\underrightarrow{\delta_\varphi=a_0^\varphi(\varphi-\varphi_{pr})}\quad\delta_\varphi>0\rightarrow M_p<0\rightarrow 低头\\
\alpha<0\rightarrow Y^\alpha\alpha=C_L^\alpha qS_M\alpha<0\rightarrow M_{st}>0\rightarrow 抑制低头，抬头
$$
![]({{site.url}}/images/img_0726/img/003.png)

静不稳定时，发动机偏角$\delta_\varphi>0,M_p<0$，低头，$\alpha<0,M_{st}<0$，低头，俯仰角$\varphi$减小，直至$\varphi<\varphi_{pr}$，此时发动机偏角$\delta_\varphi>0,M_p>0$，但此时攻角依旧<0，两个M平衡。体轴先在指令轴和速度轴之间，后来在指令轴之下。

![]({{site.url}}/images/img_0726/img/004.png)

# 飞行程序设计

## 飞行程序

通过设计攻角的程序角，得到主动段飞行时的俯仰角变化规律

垂直起飞后逐渐转弯：法向过载和控制力较小，速度的阻力损失和重力损失不至于过大

### 基本原则

垂直起飞

限制火箭转弯时的法向过载，采用重力转弯：跨音速，大动压段攻角尽可能小=0，只在重力法向分量下转弯。减小推力偏离速度方向的攻角速度损失（推力全部用于加速）

程序俯仰角连续变化，角速度和角加速度有限制

保证可靠的分离条件与合适的载入条件  分离期间姿态稳定，满足射程和弹道倾角的约束。

## 主动段

主动段分为垂直上升、转弯、瞄准/分离

<img src="{{site.url}}/images/img_0726/img/002.png" style="zoom:50%;" />

### 垂直上升段

程序俯仰角一直为90

主要参数：垂直段结束时间。过大：转弯所需过载大；过小：姿态控制能力不足

### 转弯段设计

设计参数：程序攻角，再分为两个阶段

- 有攻角的转弯，有攻角才能把火箭从90度改变。这个阶段必须要在跨音速之前结束，**减少气动载荷**和气动干扰。在这段时间内，攻角<0，绝对值由0变大再回到0，要求攻角绝对值最大的时候$t_m$不能太大，否则动压大
- 高动压区，重力转弯

### 瞄准段

主动段终点的速度倾角取最小能量弹道的倾角

# 摄动制导

![]({{site.url}}/images/img_0726/img/005.png)

主动段-自由段-再入段

**主动段制导任务**：给出姿态角指令，使火箭在关机点的运动参数满足条件，满足命中目标的要求

## 关机方程

$F(r,v,r_T)=0$，状态不唯一，$X(t)=r,v,r_T$

射程偏差关机方程：取射程偏差=弹目实际距离-预估射程，为关机方程的函数，

关机方程：$\Delta L(X(t))$；关机点：$\Delta L(X(t_k))=0$

## 摄动制导

摄动：将一个函数写成在给定参数或者变量附近的近似表达式

关机方程在关机点的一阶泰勒展开
$$
\Delta L(X(t))=\Delta L(\bar X(\bar t_k))+\frac{\partial \Delta L}{\partial \bar X(\bar t_k)}[X(t)-\bar X(\bar t_k)]=\frac{\partial \Delta L}{\partial \bar X(\bar t_k)}[X(t)-\bar X(\bar t_k)]\tag{1}\label{guanjii}
$$
判断以上方程是否为0

离线设计标称弹道$\bar X(\bar t)$，和标称关机点$\bar t_k$，离线计算在标称弹道关机点处$\bar X(\bar t_k), \frac{\partial \Delta L}{\partial \bar X(\bar t_k)}$

当实际飞行时间接近于标称关机时间，开始计算$\eqref{guanjii}$，$X(t)$从导航信息实时获得

<img src="{{site.url}}/images/img_0726/img/006.png" style="zoom:67%;" />

## 导引方程

当建模误差和外部干扰过大时，线性近似不准确。为了抱枕线性关机方程的有效性，设计导引方程，调整弹体姿态角，使实际关机点在标称关机点附近。

**摄动制导原理流程图**

![]({{site.url}}/images/img_0726/img/007.png)

# 摄动制导基础

### 偏差微分变分

全偏差：**两个函数**在**两个时间**下的取值偏差，

微分：自变量充分小的时候函数的增量$d\xi=\dot \xi(t)dt$

变分：$d\xi(t)$为函数范数充分小的增量

全偏差$\approx$由关机时间不一致导致的偏差加上在同一时刻的等时偏差

![]({{site.url}}/images/img_0726/img/008.png)

### 线性展开

在标称关机点线性展开

### 关机时刻

$$
\Delta L[X(t_k),t_k]=\dot L[\bar X(\bar t_k),\bar t_k]\Delta t_k+\left.\frac{\partial L}{\partial X}\right|_{\bar t_k}\delta X(t_k)=0
$$

### 法向导引

由雅各比矩阵分析得到：弹道倾角$\theta$对于射程影响最大，所以需要通过控制俯仰角$\varphi$，减小$\Delta\theta(X(t_k))$，保证关机方程有效性

### 横向导引

控制偏航角$\psi$，控制火箭质心的横向方向，保证横向落点偏差$\Delta H$在容许范围内

### 预测校正框架

**预测**：根据当前状态的偏差$\delta X(t)$预测关机时刻的状态偏差$\delta X(t_k)$，从而预测关机时刻的特征量$\Delta L,\Delta\theta,\Delta H$

采用**伴随定理**，实时预测当前偏差对终端特征量的影响

**校正**：利用控制量俯仰角和偏航角，实时消除干扰量$f(t)$引起的特征量关机时刻偏差为0,$\Delta\theta=\Delta H=0$

采用**干扰抑制**原理，实时补偿干扰对终端偏差的影响

### 伴随定理

![]({{site.url}}/images/img_0726/img/009.png)

分析当前状态偏差和干扰对终端制导指标影响（弹道倾角，横向偏差）的理论基础是伴随定理

非线性动力学--线性时变系统。状态量-位置速度；控制量-俯仰角偏航角；干扰量

线性时变系统
$$
\delta\dot X(t)=A(t)\delta X(t)+B(t)\delta U(t)\tag{2}\label{LTVS}
$$
定义伴随方程
$$
\dot\Lambda(t)=-A^T(t)\Lambda(t)\tag{3}\label{bansui}
$$
则有，未来某时刻=当前时刻+此后的积分

(当伴随向量为单位矢量的时候，即为现代控制里的转移方程)
$$
\Lambda^T(t_k)\delta X(t_k)=\Lambda^T(t)\delta X(t)+\int_t^{t_k}\Lambda^T(t)B(\tau)\delta U(\tau)d\tau
$$
若定义$F[X(t_k)]$是终端时刻状态变量$X(t_k)$的函数，定义$\Lambda(t_k)=(\frac{\partial F}{\partial X})^T$，无控制$\delta U(t)=0$，则$\delta F(t_k)=\frac{\partial F}{\partial X}\delta X(t_k)=\Lambda^T(t_k)\delta X(t_k)$

简化为：
$$
\delta F(t_k)=\Lambda^T(t_k)\delta X(t_k)=\Lambda^T(t)\delta X(t)\tag{4}\label{jianhuabansui}
$$
合理选$\Lambda^T(t_k)$得到特定的特征量对于当前状态量的敏感度

摄动方程中，$\delta F$是关机方程的特征量$\delta L$和导引方程的特征量$\delta\theta,\delta H$

在式子$\eqref{jianhuabansui}$中，把特征量$F$换为$L,\theta,H$，计算$t_k$时刻的特征量。$\delta X(t)$由导航信息给出，但是$\Lambda^T(t)$未知

无法预知关机时刻$t_k$，不能直接对伴随系统进行反向积分，需要近似推导

推导过程：

已知伴随系统$\dot\Lambda(t)=-A^T(t)\Lambda(t)$；终端条件$\Lambda(t_k)=(\frac{\partial F}{\partial X})^T$

定义以$t,t_k$为双自变量的状态转移矩阵$\phi(t,t_k)$，有性质：伴随系统的解，传递性，可逆性，求导$\frac{d\phi(t,t_k)}{dt}=-A^T(t)\phi(t,t_k),\frac{d\phi(t,t_k)}{dt_k}=\phi(t,t_k)A^T(t_k)$

将$\phi(t,t_k)$对$t_k$在$\bar t_k$附近展开，$\phi(t,t_k)=\phi(t,\bar t_k)+\frac{d\phi(t,t_k)}{dt_k}|_{t_k=\bar t_k}\Delta t_k$，带入转移矩阵的伴随系统解
$$
\Lambda(t)=\phi(t,\bar t_k)\Lambda(t_k)-(-\phi(t,\bar t_k)A^T(\bar t_k)\Lambda(t_k))\Delta t_k=\Lambda_1(t)-\Lambda_2(t)\Delta t_k
$$
对于$\Lambda_1(t)$，有$\Lambda_1(\bar t_k)=\Lambda(t_k)$，$\dot\Lambda_1(t)=-A^T(t)\Lambda_1(t)$所以是原伴随方程$\eqref{bansui}$的解，可以从$\Lambda_1(\bar t_k)$反向积分

对于$\Lambda_2(t)$，有$\Lambda_2(\bar t_k)=\dot\Lambda_1(\bar t_k)=-A^T(\bar t_k)\Lambda_1(\bar t_k)$，也是原伴随方程$\eqref{bansui}$的解，可以从$\Lambda_2(\bar t_k)$反向积分

至此，把$\Lambda(t)$近似写为了$\Lambda_1(t),\Lambda_2(t)$的线性组合，这俩的终端条件在标称关机点附近，t时刻的伴随量从$t_k$反向积分得到。

### 干扰抑制

终端特征量=当前状态量引起的偏差+从当前时刻到终端时刻的（控制量+干扰量）引起的偏差

若当前状态量引起的偏差=$\Lambda^T(t)\delta X(t)=0$

则解控制量$\delta U(t)=-[\Lambda^T(t)B(t)]^{-1}\Lambda^T(t)C(t)f(t)=K_f(t)f(t)$

![]({{site.url}}/images/img_0726/img/010.png)

# 有导航信息的摄动制导

### 关机时刻预测

质心运动方程--线性展开--无控时伴随定理--近似求解等时偏差--全偏差为0，关机时刻预测

![]({{site.url}}/images/img_0726/img/011.png)

### 法向导引

法向导引策略：找当前时刻的控制量，使得未来满足某一性能。

由无控伴随定理，可以得到关机时刻的倾角偏差。$\delta\theta[X(t_k,t_k)]=\Lambda_n^T(t_k)\delta X(t_k)=\Lambda_n^T(t)\delta X(t)$

通过俯仰角偏差来消除。$\delta \varphi_L(t)=K_\varphi\Delta\theta$

在导引末端，接近$t_k$的时候，用常向量$\Lambda_n^T(t_k)$代替$\Lambda_n^T(t)$，简化计算。$\Lambda_n^T(t_k)=\left[\frac{\partial \theta}{\partial X}|_{\bar t_k}-\frac{\dot\theta[\bar X(\bar t_k),\bar t_k]}{\dot L[\bar X(\bar t_k),\bar t_k]}\frac{\partial L}{\partial X}|_{\bar t_k}\right]$

### 横向导引

$$
\delta \psi_L(t)=K_\psi\Delta H\\
\Delta H[X(\bar t_k),t_k]=\Lambda_h^T(t_k)\delta X(t_k)=\Lambda_h^T(t)\delta X(t)\underrightarrow{末端}\Lambda_h^T(t_k)\delta X(t)\\
\left.\left.\Lambda_h^T(t_k)=\left[\frac{\partial H}{\partial X}\right|_{\bar t_k}-\frac{\dot H[\bar X(\bar t_k),\bar t_k]}{\dot L[\bar X(\bar t_k),\bar t_k]}\frac{\partial L}{\partial X}\right|_{\bar t_k}\right]
$$

![]({{site.url}}/images/img_0726/img/012.png)

# 无导航信息的摄动制导

位置陀螺仪测量火箭发射惯性系下的俯仰角，偏航角和滚转角

加速度计测量火箭除了引力加速度之外的加速度在发射惯性系下的分量

火箭在发射惯性系下的位置和速度用加速度计测量值积分得到。

伴随定理，从0时刻开始，而不是从t时刻开始。

无法获取当前的状态量$X(t)$，只能从开始时间积分，直到关机

没有导航信息，所以要把运动方程中的气动力/干扰力求出来，（有导航的时候直接用f，没导航的时候要展开）

# 闭环制导

- 大气层内：气动力影响显著，引力场影响小。开环+摄动，有结构载荷约束，对关机时间、姿态角进行离线设计，在标称轨迹上进行微调。
- 大气层外：气动力影响小，引力场影响显著。无结构载荷约束（允许较大的机动），基于当前状态与终端目标实时计算制导指令。

## 需要速度和待增速度

在当前位置矢量，以需要速度关机，可以完成制导任务。需要速度是当前位置和当前时间的函数。$v_R$

待增速度：需要速度与实际速度之差.$v_{ga}=v_R-v$

求解需要速度：Lambert问题-已知初始位置，希望飞行器在目标时间到达目的位置，求解当前的需要速度。是一个非线性方程

## 导引方法

导引：将当前速度导引至需要速度$\Longleftrightarrow$将待增速度导引至0

$\dot v=a=a_p+g=\frac{F_p}{m}+g$，如何控制推力加速度$a_p$，实现导引目标

### 导引策略1

加速度$a$方向与待增速度$v_{ga}$方向相同
$$
\frac{a}{|a|}=\frac{v_{ga}}{|v_{ga}|}\\
a\times v_{ga}=0
$$
当推力远大于引力，加速度约等于推力加速度
$$
\boldsymbol{F}_p=F_p\frac{\boldsymbol a_p}{|a_p|}=F_p\frac{\boldsymbol v_p}{|v_p|}
$$

### 导引策略2 叉积导引

待增速度导数负方向与待增速度方向相同。即消除待增速度。
$$
\frac{\dot v_{ga}}{|\dot v_{ga}|}=-\frac{v_{ga}}{|v_{ga}|}\\
\dot v_{ga}\times v_{ga}=0\\
\dot v_{ga}=\dot v_R-g-a_p
$$
推力加速度大小$a_p$不够大时，误解，无法使用叉积导引。

### 导引策略3

将两种策略相结合
$$
c(t)a\times v_{ga}+(1-c(t))\dot v_{ga}\times v_{ga}=0
$$

![]({{site.url}}/images/img_0726/img/013.png)

## 基于需要速度的闭环制导，Q制导框架

通过控制，实时消除待增速度

导引策略：找到推力矢量方向与待增速度方向的关系，找到推力发动机的开启关闭时间

在关机后，当前速度一直等于需要速度，待增速度为0，只受引力作用，所以需要速度的变化率等于引力加速度

定义时变矩阵Q矩阵$Q=\frac{\partial v_R}{\partial r}$，则待增速度变化率$\dot v_{ga}=-Qv_{ga}-a_p$，$v_R,r$都与时间有关，所以时变

Q制导框架：

对自由段已知末端位置速度，飞行时间，过程中加速度一直为g。从末端反向积分，得到当前时刻的需要速度。需要速度对$r(t)$求导。当引力场为常值，Q是定常的。待增速度$\dot v_{ga}$

最优控制与推力加速度的历史时间无关，只与当前时刻有关。

![]({{site.url}}/images/img_0726/img/014.png)

# 显式制导和隐式制导

显式制导：采用当前状态与目标状态，计算制导指令，**直接**使由制导指令确定的预测的轨迹满足两点边值条件。有标称轨迹的，都不是显式

隐式制导：基于特定的隐式控制函数——状态量组合与相应的**标称值**的小量偏差，计算制导指令的偏差量，**间接地**使终端状态满足目标条件。控制函数有：关机方程，轨迹倾角偏差的法向导引方程，落点横向偏差的横向导引方程。摄动制导属于隐式制导

# 大气层外制导的两点边值问题

运动：只有引力加速度和推力加速度作用的运动

两点边值：当前时刻$t_0$的位置和速度；终端时刻$t_f$的位置和速度

实际控制量：推力矢量函数，幅值和方向

用积分预测终端状态，获得推力矢量函数满足两点边值问题
$$
x(t_0)=x_0\quad \dot x(t_0)=\dot x_0\\
x(t_f)=x_f\quad \dot x(t_f)=\dot x_f\\\tag{}\label{bianzhi}
$$


# 显式制导

选择(虚拟)**控制量**：总加速度--直接设计总加速度函数$\ddot x(t)$，满足两点边值问题$\eqref{bianzhi}$。确定总加速度后，调整推理加速度使得推理加速度+引力加速度=总加速度

## 单通道总加速度函数的设计：

$$
\ddot x(t)=a_0+a_1(t_f-t)+a_2(t_f-t)^2+\cdots+a_n(t_f-t)^n+\cdots
$$

不同的制导任务中，根据需要的终端条件，将级数截断，使得可唯一确定$\ddot x(t)$的解--参数数量和方程数量匹配

需要满足的两个方程，则将自由度确定为两个$\ddot x(t)=c_1p_1(t)+c_2p_2(t)$（线性无关）
$$
\dot x_f-\dot x_0=\int_{t_0}^{t_f}\ddot x(t)dt=f_{11}c_1+f_{12}c_2\\
x_f-x_0-\dot x(t_0)t_{go}=\int_{t_0}^{t_f}\left[\int_{t_0}^{t}\ddot x(s)ds\right]dt=f_{21}c_1+f_{22}c_2
$$
求解出$c_1,c_2$，则$a_{Px}(t)=\ddot x(t)-g_x(t)=c_1p_1(t)+c_2p_2(t)-g_x(t)$

### 积分计算技巧

对于函数$\ddot x(t)=a_0+a_1(t_f-t)+a_2(t_f-t)^2+\cdots+a_n(t_f-t)^n+\cdots$

一次积分$\dot x_f-\dot x_0=\int_{t_0}^{t_f}\ddot x(t)dt$，结果，对于$a_i$项：被积函数中对应多项式系数为$i$，积出来之后多项式对应为$\frac 1{i+1}a_it_{go}^{i+1}$

二次积分$x_f-x_0-\dot x(t_0)t_{go}=\int_{t_0}^{t_f}\left[\int_{t_0}^{t}\ddot x(s)ds\right]dt$，对于$a_i$项：被积函数中对应多项式系数为$i$，积出来之后多项式对应为$\frac 1{i+2}a_it_{go}^{i+2}$

对于k次积分，每一项为$\frac 1{(i+k)}\frac1{(k-1)!}a_it_{go}^{i+k}$，验证程序见`poly_int.m`

### 预测校正框架

$$
\begin{bmatrix}c_1\\c_2\end{bmatrix}=\begin{bmatrix}e_{11} & e_{12}\\e_{21}&e_{22}\end{bmatrix}\begin{bmatrix}\text{预测的终端速度误差}\\\text{预测的终端位置误差}\end{bmatrix}
$$

预测的终端速度/位置误差，是在总加速度为0（无控）的情况下的误差$\dot x_f-\dot x_0,x_f-x_0-\dot x(t_0)t_{go}$

E矩阵为原来F矩阵的逆矩阵，附二阶矩阵求逆
$$
F=\begin{bmatrix}a&b\\c&d\end{bmatrix}\quad F^{-1}=\frac1{det(F)}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}
$$
矩阵求逆：求出每个位置上的代数余子式（正负一交错），取转置，再除以行列式

### 系数更新

如果当前的位置速度准确，，引力场模型准确，$c_1,c_2$无需更新

如果位置速度精确度逐渐增加，则需要更新

### E矩阵分析

当$t_{go}$越来越小，则每个元素越来越大。但预测的终端误差会变小，所以c不会由于$t_{go}$的变小而变大（理想情况下，c不会变化）

但实际情况下，终端误差不会趋于0，c就会变大。所以在最后几秒，停止对E和c更新

## 发动机推力可调

给定三轴推力加速度$\boldsymbol a_P=[a_{Px}\quad a_{Py}\quad a_{Pz}]^T=\frac{F_P}m\begin{bmatrix}\cos\varphi_c\cos\psi_c\\\sin\varphi_c\cos\psi_c\\-\sin\psi_c\end{bmatrix}$

解出推理大小，俯仰角、偏航角指令

## 实例

取$p_1(t)=1,p_2(t)=t_f-t$

可以解得x轴需要的总加速度，同理另外三轴

# 最优显式制导

自由度大于约束数目时，能进行最优控制--遍历$a_i$找到燃料消耗最小的参数（效率低，离线计算）

# 火箭姿态控制

![]({{site.url}}/images/img_0726/img/015.png)

![]({{site.url}}/images/img_0726/img/016.png)

## 动力学特征

绕质心运动：刚体运动+推进剂晃动（影响姿态）+弹体弹性振动（各类激励，固有振型）

受力：引力、气动力、推力、控制力、摆动惯性力、干扰力

力矩：气动力矩，推力矩，控制力矩，摆动惯性力矩，干扰力矩

### 引力

不产生力矩，作用在质心上。将引力从发射点惯性坐标系投影到速度系

### 气动力和气动力矩

在速度系分量为阻力升力侧向力$F=CqS_M$

C有阻力系数、法向力对攻角的偏导，侧向力对偏航角的偏导

几个角度关系：体轴，地速，气流速度。气流速度=地速+风速

无风时攻角$\alpha_0$地速与体轴夹角；风速带来的附加攻角$\alpha_w$地速气流速度夹角；总攻角$\alpha$气流速度与体轴夹角

质心压心不重合，气动力矩分为稳定力矩和阻尼力矩：气动力作用到压心上，产生稳定力矩；火箭转动，存在阻尼

![]({{site.url}}/images/img_0726/img/017.png)

### 推力

由于摆角小，所以近似沿体轴。但研究对于姿态控制的时候，小摆角能提供足够的控制力矩。

不产生力矩

### 控制力与控制力矩

摆角受力方向相反，定义正摆角（x前，y上，z右）

写出三轴力矩和摆角的关系$\boldsymbol M_c=\sum_i\boldsymbol B_i\delta_i$，Bi是每个舵单位偏角对三轴的力矩矢量

$z_c$是发动机作用点与火箭纵轴的距离，$x_c$是理论尖端到发动机作用点的距离，$x_c-x_g$是yz轴的力臂

定义等效舵偏（实际不存在）

两台发动机偏航俯仰，四台发动机滚转，正偏角产生负力矩
$$
\begin{cases}
F_{cxb}=2p\cos\delta_{\varphi}+2p\cos\delta_{\psi}-F_p\\
F_{cyb}=2p\sin\delta_{\varphi}\\
F_{czb}=-2p\sin\delta_{\psi}
\end{cases}
\begin{cases}
\bar M_{cxb}=-4pz_c\delta_r\\
\bar M_{cyb}=F_{czb}(x_c-x_g)=-2p(x_c-x_g)\sin\delta_{\psi}\\
\bar M_{czb}=-F_{cyb}(x_c-x_g)=-2p(x_c-x_g)\sin\delta_{\varphi}\\
\end{cases}
$$
设计等效舵$\bar M=\sum_i\boldsymbol B_i\delta_i$

偏角都为小量，不定方程，引入辅助方程 俯仰舵和偏航舵产生的滚转力矩相同
$$
pz_c(\delta_3-\delta_1)=pz_c(\delta_4-\delta_2)
$$
四个物理舵摆角为在其对应俯仰偏航综合摆角的基础上，叠加滚转通道（俯仰与偏航的差动）的综合摆角

### 发动机惯性力与惯性力矩

发动机在摆动的时候会产生惯性力和惯性力矩

### 干扰力与干扰力矩

$\Delta C,\alpha_w,\beta_w$等不确定因素用干扰力等效

### 液体晃动动力学

用弹簧振子模型来描述复杂的液体晃动

### 弹性振动

![]({{site.url}}/images/img_0726/img/018.png)

较高的长细比，较小的结构质量，结构刚度小，在外力作用下产生弹性振动。姿态控制时考虑振动的影响

弹性振动产生的横向位移和一系列弹性振型（不同频率）产生的位移叠加

弹性形变通过影响速率陀螺的测量影响火箭的姿态稳定性--关注位移

对姿态测量角$\Delta \varphi_s=\Delta \varphi+\varepsilon$
$$
\varepsilon=-\left.\frac{\partial y(X,t)}{\partial X}\right|_{X=X_s}=-\sum_{i=1}^nq_i(t)W'_i(X_s)
$$
对姿态角速率$\dot \Delta \varphi_s=\dot\Delta \varphi-\sum_{i=1}^nW'_i(X_s)\dot q_i$

**速率陀螺仪理想的安装位置在$W'(X_s)=0$处**

还可以进行滤波

## 姿态控制

![]({{site.url}}/images/img_0726/img/019.png)

任务：根据制导系统和导航系统提供的信号控制弹体的姿态角

GNC任务：在干扰作用下沿着预先选定的标准弹道飞行，偏差在允许的范围内

前期：不饿能调节推力大小，主要靠控制弹体的推力方向。因为推力方向是由刚性弹体的姿态角决定的

### 姿态动力学特点

- 动力学模型复杂，阶次高
- 特征参数时变
- 飞行环境复杂且存在干扰和不确定性
- 结构刚度低，低频特性可能存在耦合（液体晃动，弹性）

# 稳定性

稳定：偏离平衡状态，能自己回到平衡状态

李雅普诺夫稳定：初值在一定范围内，其后所有的状态都在一个范围内

线性定常稳定：特征多项式零点在左半平面（劳斯，林判据）

## 受扰运动的稳定性

基于标称轨迹的李雅普诺夫稳定性

初始条件在一定范围内，其后的状态都在一个范围内

非线性时变-->在标称轨迹附近展开，线性定常，再分析稳定性

## 系数冻结

系数冻结分析线性时变的稳定性

绕质心运动的暂态过程比线性时变系统的系数变化快，认为在一定时间内，方程系数不变化，视为常微分

- 最大动压飞行段（静不稳定度最大）
- 弹性振动频率与刚体运动频率最接近
- 弹性振动和液体晃动频率最接近
- 发射，分离，发动机开关机，

# 线性化

标称、实际轨迹偏差为小量，解耦成三个互相独立平面的运动（俯仰偏航滚转）

| 俯仰                         | 偏航                      | 滚转                        |
| ---------------------------- | ------------------------- | --------------------------- |
| 弹道倾角$\theta$             | 航迹偏航$\sigma$          |                             |
| 攻角$\alpha$                 | 侧滑角$\beta$             |                             |
| 俯仰角$\varphi$              | 偏航角$\psi$              | 滚转角$\gamma$              |
| 发动机俯仰角$\delta_\varphi$ | 发动机偏航角$\delta_\psi$ | 发动机滚转角$\delta_\gamma$ |

> 对哪个通道进行分析，哪个通道就不是小量$\theta=\theta_0+\Delta\theta$，其他通道是小量$\sigma=\Delta\sigma$

按照火箭的运动特点，偏航和滚转为小量

不是小量：基准+偏差；小量：基准=0，偏差

先简化角速度$\omega_x,\omega_y,\omega_z$

写出俯仰通道方程，带入简化角速度和线性化变量（标准+小量），进行简化

写出俯仰通道标称弹道，即将变量写为 标准 （没有小量），进行简化

上面两个式子相减，得到摄动方程

还有小角度假设的几何关系$\Delta\varphi=\Delta\alpha+\Delta\theta$，即可写出$\Delta\dot\theta,\Delta\ddot\varphi,\Delta\varphi$与其他变量的关系

$b_2$是气动力矩对$\Delta\ddot\varphi$的作用系数。$b_2$前面有一个负号，所以大于0，静稳定。

将变量写为$X=\begin{bmatrix}\Delta\theta&\Delta\varphi&\Delta\dot\varphi\end{bmatrix}$，则可写为单输入三输出形式$\dot X=AX+B\Delta\delta_{\varphi}$

# 稳定性分析

将以上状态空间表达式拉式反变化，得到简化的特征方程（线性时变）

用系数冻结法，给出几个关键在特征点，判断简化的特征方程是否稳定

轨迹运动为长周期，姿态运动为短周期

## 起飞

速度小，质心运动方程系数c大(v在分母)，绕心运动方程系数b小($q=\frac12\rho v^2$在分子)，阻尼项小，忽略气动阻尼$b_1$，将长周期状态方程提出来，成为一个一节系统*二阶系统

系统不稳定。$b_2<0$一对共轭复根在右半平面，震荡发散；$b_2>0$一实根在右半平面，单调发散

长周期量（弹道倾角）在三个模态下的占比最大

## 气动力矩系数最大

v大，c小，b大

长短周期分离，侧重体现短周期的动力学特征

$b_2>0$，二阶系统稳定，有一个实根$c_2$在右平面，重力作用下缓慢震荡发散；$b_2<0$，除了$c_2$还有一个跟在右平面，单调快速发散

## 关机前

高度高，空气稀薄，气动力矩$b$小，忽略b，在原点上右两个特征根，不稳定

关机前无控，弹体不能稳定飞行，一旦右外干扰姿态角就会增大

轨迹运动与姿态运动耦合

# GNC硬件

GNC是一体的，软硬件是一体的

三大核心硬件环节：

陀螺仪和加速度计，飞控计算机，执行机构

# 陀螺仪

基于动量矩定理，角运动检测装置

## 特性

### 定轴性

动量矩$H=J\Omega$，动量矩定理$\frac{dH}{dt}=M$，当$M=0$，动量矩守恒，主轴方向恒定

### 进动性

z方向的动量矩$H_z=J_z\Omega_z$，当受到外力矩$M_x$作用时，动量矩$H_z$朝着$M_x$方向进动，显示出圆环主轴连续转向，追赶外力矩
$$
M_x\Delta t=H_z\tan\Delta\varphi,(\Delta\varphi小量)M_x\Delta t=H_z\Delta\varphi\\
\omega=\frac{d\varphi}{dt}=\frac{M_x}{H_z}
$$
确定方向：$\omega\times H=M$

## 分类

按功能：位置（测量角度），速率（测量角速度），积分（测量角度和角速度）

按自由度：二自由度，单自由度

按原理：转子（刚体转子告诉旋转），激光（Sagnac效应），光纤（光纤取代环激光器），MEMS（半导体技术，体积小成本低大批量）

按支撑方式：滚珠轴承，气浮（静压气浮动压气浮），液浮（静浮力静压力支撑），弹性支承（消除摩擦力矩，挠性），静电支撑（对转子形成静电场，用静电力支撑）

## 原理

### 位置陀螺

**二自由度**，测量姿态角，分为垂直陀螺仪和方向陀螺仪。利用**定轴性**

- 垂直陀螺仪：测量滚转角和俯仰角

  内环轴与x轴重合，转子轴与y重合，外环与z重合。

  滚转，电位器相对转动，输出电压$u$与滚转角$\gamma$成线性$\gamma=k_\gamma u_\gamma$；俯仰角$\theta$同理

- 方向陀螺仪：测量偏航角和俯仰角

  转子轴与x轴重合，外环轴与y重合，内环与z重合。偏航角$\psi$同理

### 位置陀螺仪的漂移

$\omega_d=\frac{M_d}{H}$同上进动公式，也可以加上$\omega$方向的随机漂移
$$
\omega_{dx}=-\frac{M_{dy}}{H_z}\quad\omega_{dy}=\frac{M_{dx}}{H_z}
$$


干扰力矩$M_d$有三项

- 与加速度无关的常值力矩：
- 与加速度一次方成正比的力矩：陀螺仪质心与转轴存在偏差，飞行器加速运动时，惯性力导致干扰力矩出现。质心静不平衡位移矢量D，惯性力矢量F，干扰力矩$M_1=D\times F$
- 与加速度平方成正比的力矩：陀螺仪非等刚度在两个正交加速度作用产生。柔性张量系数矩阵C，形变位移矢量$L_s=CF$，干扰力矩$M_2=L_s\times F=(C\cdot F)\times F$

对于位置陀螺仪，绕z轴旋转，只保留xy轴的干扰力矩项

### 速率陀螺仪

利用**进动性，单自由度**做成速率陀螺仪

转子轴沿z，框架轴沿x，测量轴沿y

飞行器以角速度$\omega_y$转动时，迫使转子产生x方向的进动，产生陀螺力矩$M'$；框架轴在$M'$作用下绕x转动；当框架轴转过角度$\beta$，弹簧反抗力矩与陀螺力矩相互平衡，停止转动；测量$\beta$。

用空气阻尼器给框架引入阻尼，消除振荡现象。

稳态时$\beta=\frac Hk\omega_y$

**高细长比**火箭**弹性振动**，速率陀螺仪敏感**等效刚体纵轴转动**，和弹性形变带来的弹体纵轴的**附加转动**，即$\Delta \varphi_s=\Delta \varphi+\varepsilon$

在**多个不同位置安装速率陀螺仪**，改变多次振型的等斜效率，满足振动稳定要求

![]({{site.url}}/images/img_0726/img/020.png)

##  陀螺仪在制导控制系统中的作用

![]({{site.url}}/images/img_0726/img/021.png)

![]({{site.url}}/images/img_0726/img/022.png)

制导回路由**制导系统、控制系统、执行机构、运动学环节**等组成的闭环回路

陀螺仪主要参与控制系统的校正

速率陀螺改善了阻尼

# 加速度计

输出与运动载体线加速度成比例的信号。牛顿第二定律

## 原理

$$
a+g=\frac{F_\text{弹}}{m}
$$

将作用在单位质量上的惯性力和引力的矢量和，即$\frac{F_\text{弹}}{m}$定义为**比力**。加速度计实际测量的是比力$f$，而不是载体的运动加速度。所以需要**进行补偿**

## 分类

- 传统
  - 重锤式：与重锤固连的电位器相对于壳体产生位移。稳态时，敏感加速度$a$与重锤相对位移$x$关系$a=-\frac kmx$
  - 浮夜摆式：重心$C_M$和浮心$C_B$位于支撑轴(输出轴)两端，用摆轴连接。与摆性轴和支撑轴垂直的轴为输入轴。输入轴有加速度，绕输出轴的摆力矩$M_p$由重力矩和浮力矩组成。偏转角$\theta$输出电压，给力矩器产生力矩，与摆力矩平衡。当偏转角过大时，会降低所测量轴上加速度的灵敏度，还会敏感正交加速度分量，成为**交叉耦合效应**
  - 挠性：也是一种摆式，摆件弹性支承在挠性轴上。摆组件偏角应该尽量小：降低加速度测量误差，减少交叉耦合效应
- 新型
  - 压阻、雅典、振梁、激光、光纤

## 加速度计在系统中的应用

高空风会产生附加攻角$\alpha_w$，气动载荷增大，形成内力弯矩，导致火箭街斗失稳、破坏。

**减载**：通过制导控制方法，调整轨迹和姿态，使火箭*顺风飞行*，减小攻角。

关键：设计攻角反馈，实时将攻角减小至0.

通过**加速度计信息的反馈**实现攻角信息的间接反馈。

# 惯性制导

惯性导航：IMU测量的数据经过导航系统解算得到飞行器位置速度和姿态角

惯性制导：直接用敏感元件测量的数据计算关机方程和导引方程，不需要进行对位置速度姿态角进行解算。**导航、制导/控制一体化**

## 摄动制导

惯性制导是摄动制导而不是显示制导

关机函数有哪些典型的数学性质：是$r,v,r_T$的非线性函数，当$r=r_T$时=0，

在摄动假设下，采用基于标称轨迹的泰勒展开计算非线性关机函数

摄动制导的设计：离线设计标称弹道；在标称弹道附近对运动方程进行线性化，推导摄动方程；基于摄动方程，推导关机方程和导引方程

## 惯性制导原理

平台式/捷联式：区别在于摄动方程的具体实现不同

**关机方程**控制关机时间，使得终端航程满足航程*L*。需要实时计算关机特征量，与标称关机特征量进行比较。求解以航程$L[X(t_k)]$为终端指标，控制量为关机时间

**法向导引**方程求解以终端弹道倾角误差$\Delta \theta(t_k)$为指标，控制量为俯仰角

**横向导引**方程求解以终端横向位置误差$\Delta H(t_k)$为指标，控制量为偏航角

## 敏感元件的冗余配置

提高精度和可靠性的办法：提高单个元件可靠性；通过冗余增加组件的故障容许次数

正交配置：提高某特定方向的测量精度，计算误差小，制造难度低，实时性好

非正交配置：**提高导航性能和故障检测能力**；需要对IMU进行附加运算，增加了计算量，有新的计算误差

### 冗余配置的评价指标

- 导航性能：描述性能用来描述配置方案的测量误差。
- 可靠度：描述配置方案对元件故障的容错能力

# 火箭发动机

## 特性

### 动量推力

推力$T=-\dot mc$，推力=-推进剂秒耗量*发动机喷管排气速度

齐奥尔科夫斯基火箭方程
$$
v_1-v_0=c\ln\frac {m_0}{m_1}
$$
采用多级火箭：分别计算二级火箭和一级火箭的最终速度

### 比冲

发动机产生的总冲量的与消耗推进剂重量的比值。本质上还是描述喷口的排气速度。$I_{sp}=\frac{T}{g_0\dot m}=\frac{c}{g_0}$
$$
T=-\dot mc=I_{sp}\dot mg_0
$$

### 压差推力

火箭发动机产生的压差推力方向与喷管截面垂直向前，大小正比于截面积和燃烧室内外压差

### 总推力

动量推力方向和压差推力方向相同，总推力沿发动机喷管的纵轴向前$T=T_1+T_2$动量推力+压差推力

## 分类

- 液体--大比冲，大推力，可调节，可反复启动

  加压：保证推进剂能被送到燃烧室；燃烧室内压力和推力成正比，压力越大推力越大。

- 固体--中等比冲，大推力，不可调节，不可反复启动

  工作过程：点火器点火，产生热气，点燃推进剂；推进剂燃烧产生高温高压燃气；燃气经过喷管喷出，产生推力。

  特点：结构简单，可靠性高；易于贮存；不能多次启动；推理不可调节

  设计：提高初始温度，控制压力增加燃速；通过装药设计增加燃面

- 反作用力控制系统--小比冲，小推力，恒定推力脉冲工作

## 接口原理

- 推力，质量特性：参数（比冲，秒耗量，喷管面积，喷管压力）
- 关机：推力终止关机（工艺难度高）/耗尽关机（推进剂耗尽时满足制导目标，主流）

![]({{site.url}}/images/img_0726/img/023.png)

# 姿态控制

## 线性二次调节器

## 滑模控制理论

# 考试总结
tmd只给我81

回忆一下，有哪些没复习到：
- 陀螺仪与加速度无关、一次方、平方的干扰力矩的计算（纯背公式）
- 硬件部分有个啥回路还是流程图来着（不是陀螺仪加速度计的力学原理那种），我本来觉得肯定不会考，结果这是一整道大题
- 起飞阶段的稳定性分析
- 还有个啥我忘了