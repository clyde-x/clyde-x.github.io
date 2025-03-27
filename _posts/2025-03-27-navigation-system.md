---
layout: article
title: "导航系统"
tags: "考研复试"
category: kaoyan
excerpt_separator: <!--brief-->
permalink: /kaoyan/navigationsystem
image:
  teaser: teaser1.jpg
---
惯导、卫星导航、天文导航、组合导航乱七八糟的都有，挑了一些重点（也可能不是重点），不太注重公式的推导，也不是很注重概念的明晰，赶工赶出来的。
<!--brief-->
# 基础概念

## 方向余弦矩阵

两个直角坐标系之间的旋转变换可以用**方向余弦阵**描述。可以等效于绕某一固定轴的一次转动，这个固定轴和转交构成了**等效旋转矢量**

## 四元数

$$
Q=q_0+q_1i+q_2j+q_3k=q_0+q_v
$$

四元数是超复数，有实部和虚部。一个三维矢量可以看作实部为0的四元数。

四元数满足加法的交换律和结合律

乘法$P\circ Q=(p_0+p_v)\circ (q_0+q_v)=(p_0q_0-p_v^Tq_v)+(p_0q_v+q_0p_v+p_v\times q_v)$在没有歧义的情况下可以省略中间的$\circ$

乘法不满足交换律

共轭/转置：$Q^*=q_0-q_v$

2范数/模：$\vert\vert Q\vert\vert=\sqrt{Q^*\circ Q}=\sqrt{q_0^2+q_1^2+q_2^2+q_3^2},\vert\vert P\circ Q\vert\vert=\vert\vert P\vert\vert\cdot \vert\vert Q\vert\vert$

逆：$Q^{-1}=\frac{Q^*}{\vert\vert Q\vert\vert^2},(P\circ Q)^{-1}=Q^{-1}P^{-1}$

四元数与方向余弦矩阵的关系：
$$
\begin{bmatrix}
q_0^2+q_1^2-q_2^2-q_3^2 & 2(q_1q_2-q_0q_3) & 2(q_1q_3+q_0q_2) \\
2(q_1q_2+q_0q_3) & q_0^2-q_1^2+q_2^2-q_3^2 & 2(q_2q_3-q_0q_1) \\
2(q_1q_3-q_0q_2) & 2(q_2q_3+q_0q_1) & q_0^2-q_1^2-q_2^2+q_3^2
\end{bmatrix}
$$

## 常用坐标系

|                         | 原点       | x                      | y          | z                    | 备注                                                         |
| ----------------------- | ---------- | ---------------------- | ---------- | -------------------- | ------------------------------------------------------------ |
| 地心惯性系i, inertial   | 地心       | 赤道平面内指向春分点   | 赤道平面内 | 地球自转轴，指向北极 | 惯性传感器的输出就是以此坐标系为参考。准惯性系，有微小可忽略角速度 |
| 地球坐标系e, earth      | 地心       | 赤道面内指向本初子午线 | 赤道面内   | 自转轴，指向北极     | 也叫地心地固坐标系ECEF，有角速度                             |
| 地理坐标系g，geographic | 运载体质心 | 东e                    | 北n        | 天u                  | g相对于e可由运载体的经纬高表示                               |
| 导航坐标系n，navigation |            |                        |            |                      | 在求解导航参数的参考坐标系，长时间只能进行水平定位。         |
| 本体坐标系b，body       | 运载体质心 | 沿横轴向右             | 沿纵轴向前 | 沿载体轴向上         | b与n的关系可以用欧拉角表示                                   |

# 地球与重力

地球近似为旋转椭球体，赤道宽两极窄

# 惯性导航

平台式GINS：将惯性器件安装在惯性平台上，惯性平台能隔离载体的角运动和角振动

捷联式SINS：工作环境恶劣，精度低。加速度计的输出沿载体坐标系，需要转到导航系。

## 器件

陀螺仪：有二自由度和单自由度

性质：定轴性和进动性

表观运动：因为地球地面不是惯性系，观察者以地球作为参考基准所看到的这种表面上的进动现象，叫做陀螺仪的表观进动。**每24小时进动一周**。地球上观察到的转子陀螺自转轴以$-\omega_{ie}$的角速度做旋转，旋转所形成的曲面为一圆锥面，**对称轴平行于地轴**，半锥角为 *θ* ，陀螺的这种运动称为表观运动。

进动：$\frac{dH}{dt}=M$，进动角速度$w=\frac MH$

## 姿态更新

载体的姿态角用n相对b系的三次转动$\varphi,\theta,\gamma$（航向，俯仰，滚转），姿态矩阵$C_n^b$是时变的，为了确定姿态，需要随时解算一个四元数的运动方程：$\dot q=\frac12q\circ\omega_{nb}^b$

其中$\omega_{nb}^b$是角速度，但陀螺输出的是b相对于i的角速度$\omega_{ib}^b$，有以下关系：
$$
\omega_{nb}^b=\omega_{ib}^b-C_n^b\omega_{in}^n=\omega_{ib}^b-C_n^b(\omega_{ie}^n+\omega_{en}^n)
$$
n系相对于i系的旋转，包含地球自转引起的导航系旋转+惯导系统在地球表面附近移动引起的n系旋转
$$
w_{ie}^n=[0, w_{ie}\cos L,\omega_{ie}\sin L]^T\\
\omega_{en}^n=[-\frac{v_N}{R_M+h},\frac{v_E}{R_N+h},\frac{v_E}{R_N+h}\tan L]^T
$$

## 比力方程

$$
\dot v_{en}^n=C_b^nf_{sf}^b-(2\omega_{ie}^n+\omega_{en}^n)\times v_{en}^n+g^n
$$

其中$f_{sf}^b$是加计测量的比力；$(2\omega_{ie}^n+\omega_{en}^n)\times v_{en}^n$是载体运动和地球自转引起的哥氏加速度+载体运动引起的对地向心加速度；g是重力加速度。后两项统称有害加速度。

在加计的输出中扣除有害加速度之后才能获得载体在导航系下的加速度

## 误差传播特性

惯性传感器测量误差：$\nabla,\varepsilon$分别为加计和陀螺仪的零偏/零漂，作为随机常值（导数为0）

姿态误差方程：$\dot\phi_E,\dot\phi_N,\dot\phi_U$，反映计算导航系（n‘）相对于理想导航系的失准角$\phi$的变化

速度误差方程：$\delta\dot v_E,\delta\dot v_N,\delta\dot v_U$

位置误差方程：$\delta \dot L,\delta\dot\lambda,\delta\dot h$

在**静基座**下，惯导的真实速度$v^n=0$，真实位置（经纬高）准确已知，比力在导航系$f_{sf}^n=[0,0,g]^T$，地球近似为球体R，可以将上述方程简化解耦：

1 垂直通道不稳定，不考虑。2 经度误差与其他误差解耦，单独考虑 3 其他误差由以下状态方程描述：
$$
\begin{gathered}
\boldsymbol{X}=
\begin{bmatrix}
\phi_\mathrm{E} & \phi_\mathrm{N} & \phi_\mathrm{U} & \delta v_\mathrm{E} & \delta v_\mathrm{N} & \delta L
\end{bmatrix}^\mathrm{T} \\
\boldsymbol{U}=
\begin{bmatrix}
-\varepsilon_\mathrm{E} & -\varepsilon_\mathrm{N} & -\varepsilon_\mathrm{U} & \nabla_\mathrm{E} & \nabla_\mathrm{N} & 0
\end{bmatrix}^\mathrm{T} \\
\boldsymbol{F}=
\begin{bmatrix}
0 & \omega_\mathrm{U} & -\omega_\mathrm{N} & 0 & -1/R & 0 \\
-\omega_\mathrm{U} & 0 & 0 & 1/R & 0 & -\omega_\mathrm{U} \\
\omega_\mathrm{N} & 0 & 0 & \tan L/R & 0 & \omega_\mathrm{N} \\
0 & -g & 0 & 0 & 2\omega_\mathrm{U} & 0 \\
g & 0 & 0 & -2\omega_\mathrm{U} & 0 & 0 \\
0 & 0 & 0 & 0 & 1/R & 0
\end{bmatrix}\\
\dot{\boldsymbol X}={\boldsymbol F}{\boldsymbol X}+{\boldsymbol U}\\
\delta\dot\lambda=\frac{\delta v_E}{R}\sec L
\end{gathered}
$$
拉普拉斯变换之后分析，全部是虚根，为无阻尼震荡系统，包含地球自转、休拉(Schuler)$\omega_s=\sqrt{g/R}$，傅科(Foucault)$\omega_f=\omega_{ie}\sin L$三个震荡周期

# 卫星导航

GNSS分为地面监测网络、空间卫星星座、用户GNSS接收机三部分。

地面监测网络：主控站、监测站、注入站，对星座进行跟踪，修正导航电文，提供时间基准

基本原理：用户GNSS接收到卫星发射的导航信号，测定由卫星到接收机的延迟，或者测定载波信号的相位差，解算出接收机到卫星之间的距离，确定接收机位置。

伪距：含误差的GNSS测量距离

## 信号的基本结构

GPS信号分为测距码（P码和C/A码），数据码（导航电文D码），载波（L1载波和L2载波）

测距码和数据码调制在载波上，分别用伪随机噪声码来测距，发送数据

**导航电文**：

一个主帧30s，包含5个子帧。123子帧内容每小时更新一次，包含时钟修正参数、星历表等；45子帧的内容仅当给卫星注⼊新的导航电⽂后才得以更新，包含卫星历书等。

一个子帧6s，包含10个字

一个字0.6s，包含30bit

每帧电文由1500bit，播送速度50bit/s，每帧播送时间30s

**伪随机噪声码**：

具有随机码序列良好相关特性的有周期性的序列，具有随机码的良好自相关性，又具有某种确定的编码规则，是周期性的，容易复制。伪随机噪声码由多级反馈移位寄存器产生

线性反馈移位寄存器产生得到周期最长的二进制序列称为m序列，是最简单最容易实现的一种周期性伪随机序列，易产生，规律性强，有良好自相关和互相关特性。

## 伪距定位

**三个时间**：1 GPS信号的发射时间 2 GPS信号的接收时间 3 GPS时间（作为统一的时间基准保证卫星和接收机时钟同步）

伪距$\rho=r+c\Delta t,r=c\tau$，r是实际距离，$\Delta t$是用户时钟相对于卫星时钟的钟差。$\tau$是电波实际的传播时间，包含$(t-\tau)$时刻卫星位置与t时刻用户位置距离/c，还有电离层延时I，对流层延时T。

有四个未知参数，用户接收机的三轴坐标，和用户接收机的钟差。所以至少需要四颗星得到四个独立的方程。在求解时，构建观测矢量的方向余弦矩阵G，最小二乘，牛顿迭代求解位置和钟差。

## 误差分析

假设测量误差零均值高斯，定位误差的协方差矩阵的权重系数矩阵$H=(G^TG)^{-1}$只与卫星分布有关。只关注H矩阵对角线元素$h_1,h_2,h_3,h_4$，可以构建不同形式的精度因子DOP:
$$
GDOP=\sqrt{h_1^2+h_2^2+h_3^2+h_4^2}几何位置;\\
PDOP=\sqrt{h_1^2+h_2^2+h_3^2}位置;TDOP==\sqrt{h_4^2}时钟误差\\
HDOP=\sqrt{h_1^2+h_2^2}水平位置;VDOP=\sqrt{h_3^2}垂直位置
$$
**选星**

当接收机追踪的卫星多于4时，应当选择GDOP最小的一组卫星观测。选星的原则：观测卫星的仰角不小于5~10度，GDOP最小。计算选星或者按照几何图形选星。

**误差来源**

与卫星有关：星历误差，卫星钟误差，相对论小于

与信号传播有关：电离层对流层，多路径

与接收机有关：钟误差，位置误差，天线相位中心

其他误差：地球潮汐，负荷潮

根据性质，分为系统误差和偶然误差。系统误差解决：引入未知参数，并求解；建立系统误差模型加以修正；不同观测站对相同卫星的同步观测值求差；忽略。解决偶然误差，包括多路径效应和观测误差等：选用好硬件和观测条件，延长观测时间。

**多路径**：接收到卫星直接发射的信号和经过天线周围反射的卫星信号。与测站环境、反射体性质、接收机性能有关。避开强反射面（水面、平坦地面、光滑建筑物面），选择造型事宜频闭良好的天线，延长观测时间，改善接收机电路。

## 绝对定位和相对定位

相对定位：在两个或多个点上，同时设置接收机，各站同步观测相同的卫星，以确定两点间在坐标系的相对位置或两点间的基线⽮量。

理论依据：距离不太远的两个测站同步观测卫星时观测误差有较强相关性，星历误差、卫星钟差、接收机钟差、电离层对流层延迟基本相同

有两种方式：**1**：两点各⾃根据直接观测值，组成观测误差⽅程，各⾃解算出点位坐标；然后求两点间的坐标差，即两点的相对位置。在已知其中⼀点坐标时，即可求得另⼀点的坐标。**2**：将直接观测值进⾏不同的线性组合，先构成虚拟观测值，然后组成观测误差⽅程，进⾏相对定位解算。分为单差（两站同步观测同一卫星）、双差（两站同步观测两颗卫星）、三差（两站在两个相邻历元同步观测两颗卫星）

## 差分定位

由⽤户接受基准站发送的改正数，并对观测站的测量进⾏改正以获得精密定位的结果。根据系统服务的地理范围来分，差分定位通常被分为局域、区域和⼴域三⼤类，它们分别对应不同⻓度的基线距离。

# 天文导航

## 几何

**等高圆**

观测恒星得到仰角/高度角h，在地心以90-h为锥角画圆锥，圆锥与半径R+H的球交于一个等高圆。观测多颗恒星得到多个等高圆，相交

**纯几何**

得到恒星和近天体的矢量夹角，以近天体为顶点，以夹角为锥角画圆锥。对第二颗恒星和相同的近天体，两个圆锥相交得到两条线，排除掉一条。选另一个近天体，得到位置。

## 基于轨道动力学

直接敏感地平，利用星光间接敏感地平。在航天器轨道动力学方程和天体测量信息的基础上，利用滤波方法精确估计位置。

## 定姿

双矢量和多矢量，利用观测到的不共线的矢量进行定姿。两个不共线的矢量在导航系和载体系（观测系）中分量表达形式不同，可以由此得到两个系的旋转矩阵。

# 滤波

## 最优估计

状态$X$的估计$\hat X$是对样本的观测$Z$的函数，估计的误差$\tilde X=X-\hat X$在某一准则下，按照统计意义使得估计达到最优，有最小方差估计、极大似然估计、极大后验估计等。

最小方差：无偏，估计误差的方差与估计值的均方差完全相等。$J(\hat X)=E[\hat X^T\hat X]=min$

极大似然估计：已知$X=x$条件下观测量$Z$的条件概率密度$p(z\vert x)$。对某一具体观测值$z$而言，似然函数$L(x)=p(z\vert x)$仅仅是x的函数，当似然函数取得最大值时，将x视为X的最优估计

极大后验估计：若已知条件概率密度$p(x\vert z)$，并使其最大为准则。给定某一观测值$Z=z$，使条件概率密度函数$p(x\vert z)$达到极大的那个x值就是最优的估计。可以通过Bayes公式$p(x|z)=\frac{p(z|x)p_X(x)}{p_Z(z)}$

加权最小二乘估计：$J(\hat X)=(Z-H\hat X)^TW(Z-H\hat X)=min$

贝叶斯估计：损失函数$L(\tilde X)=L(X-\hat X)$是观测样本的函数，当样本取值不同时，带来的损失不同，定义贝叶斯风险$R(\hat X)=E[L(\tilde X)]$，使贝叶斯风险最小的估计是贝叶斯估计

## 卡尔曼滤波

状态空间模型：
$$
\begin{aligned}&\boldsymbol X_{k}=\boldsymbol{\Phi}_{k/k-1}\boldsymbol{X}_{k-1}+\boldsymbol{\Gamma}_{k/k-1}\boldsymbol{W}_{k-1}\\&\boldsymbol Z_{k}=\boldsymbol{H}_{k}\boldsymbol{X}_{k}+\boldsymbol{V}_{k}\end{aligned}
$$
噪声$W,V$是零均值的高斯白噪声，互不相关，协方差矩阵分别为Q和R。要求Q非负定，R正定

卡尔曼滤波总结为五个公式：状态一步预测，状态一步预测均方误差矩阵，滤波增益，状态估计，状态估计均方误差矩阵
$$
\hat{\boldsymbol X}_{k/k-1}=\boldsymbol{\Phi}_{k/k-1}\hat{\boldsymbol X}_{k-1}\\
\boldsymbol P_{k/k-1}=\boldsymbol{\Phi}_{k/k-1}\boldsymbol{P}_{k-1}\boldsymbol{\Phi}_{k/k-1}^\mathrm{T}+\boldsymbol{\Gamma}_{k-1}\boldsymbol{Q}_{k-1}\boldsymbol{\Gamma}_{k-1}^\mathrm{T}\\
\boldsymbol K_{k}=\boldsymbol P_{k/k-1}\boldsymbol H_{k}^{\mathrm{T}}(\boldsymbol H_{k}\boldsymbol P_{k/k-1}\boldsymbol H_{k}^{\mathrm{T}}+\boldsymbol R_{k})^{-1}\text{或简写为} \boldsymbol K_{k}=\boldsymbol P_{XZ,k/k-1}\boldsymbol P_{ZZ,k/k-1}^{-1}\\
\hat{\boldsymbol{X}}_k=\hat{\boldsymbol{X}}_{k/k-1}+\boldsymbol{K}_k(\boldsymbol{Z}_k-\boldsymbol{H}_k\hat{\boldsymbol{X}}_{k/k-1})\\
\boldsymbol P_k=(\boldsymbol I-\boldsymbol K_k\boldsymbol H_k)\boldsymbol P_{k/k-1}
$$
卡尔曼滤波有两个计算回路，独立的增益计算回路，依赖于增益回路的滤波计算回路。

## 扩展卡尔曼滤波

适用于非线性的系统
$$
\begin{aligned}&\boldsymbol{X}_{k}=f(\boldsymbol{X}_{k-1})+\boldsymbol{\Gamma}_{k-1}\boldsymbol{W}_{k-1}\\&\boldsymbol{Z}_{k}=\boldsymbol{h}(\boldsymbol{X}_{k})+\boldsymbol{V}_{k}\end{aligned}
$$
状态X在k-1时刻的参考值/标称值$X_{k-1}^n$与真实值的偏差为$\Delta X_{k-1}=X_{k-1}-X_{k-1}^\mathrm{n}$，状态预测的偏差$\Delta X_{k}=X_{k}-X_{k/k-1}^\mathrm{n}$

将系统的非线性函数f在k-1时刻的参考值$X_{k-1}^n$邻域附近展开一阶泰勒，将偏差量$\Delta X_{k}=X_{k}-X_{k/k-1}^\mathrm{n},\Delta X_{k-1}=X_{k-1}-X_{k-1}^{\mathrm{n}}$当作新的状态量，将量测的偏差$\Delta Z_k=Z_k-Z_{k/k-1}^n$当作新的量测，，构建为一个新的线性系统
$$
\begin{aligned}&\Delta\boldsymbol{X}_{k}=\boldsymbol{\Phi}_{k/k-1}^{\mathrm{n}}\Delta\boldsymbol{X}_{k-1}+\boldsymbol{\Gamma}_{k-1}\boldsymbol{W}_{k-1}\\&\Delta\boldsymbol{Z}_{k}=\boldsymbol{H}_{k}^{\mathrm{n}}\Delta\boldsymbol{X}_{k}+\boldsymbol{V}_{k}\end{aligned}
$$
此时的$\Phi_{k/k-1}^n$是非线性函数的雅可比矩阵$J(f(X_{k-1}^n))$，H同理，是h的雅可比矩阵。

## 无迹卡尔曼

扩展卡尔曼受到线性化和雅可比矩阵的计算的影响

假设一个离散的非线性系统
$$
x_{k+1}=f(x_k,u_k,k)+\omega_k\\
y_k=h(x_k,u_k,k)+v_k
$$
对非线性系统有良好的滤波效果，但计算量大，实时性不高