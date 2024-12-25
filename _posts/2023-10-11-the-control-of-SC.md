---
layout: article
title: "航天器控制原理"
tags: "BUAA课内"
category: BUAA_course
excerpt_separator: <!--brief-->
permalink: /BUAA/hangtianqikongzhiyuanli
---
这是由胡维多教授开设的一门中英双语专业选修课。老师很有意思，期末的考核也就是一篇论文
<!--brief-->

By position and velocity vectors $\vec r,\vec v$, orbital elements ($a,e,i,\Omega,\omega,\theta$) can be determined. Equally, by orbital elements, position and velocity vectors can also be determined.

## orbit elements 

First of all, we have to know what the orbital elements means (take ellipse orbit as an example):

| symbol              | mean                         | 中文       |
| ------------------- | ---------------------------- | ---------- |
| $a$                 | semi-major axis              | 半长轴     |
| $\vec e$            | eccentricity vector          | 偏心率矢量 |
| $i$                 | inclination                  | 轨道倾角   |
| $\Omega$            | longitude of ascending node  | 升交点赤经 |
| $\Pi=\Omega+\omega$ | longitude of periapsis       | 近地点赤经 |
| $\omega$            | argument of periapsis        | 近地点辐角 |
| $\theta$            | true anomaly                 | 真近点角   |
| $u_t=\omega+\theta$ | argument of latitude         | 纬度辐角   |
| $\vec H$            | the angular momentum vector  | 动量       |
| $\vec n$            | the vector of ascending node | 升交点矢量 |
| $\vec r$            | the position vector pf SC    | 位置矢量   |

<img src="{{site.url}}/images/the-control-of-space-craft/image-20230923153742620.png" alt="image-20230923153742620" style="zoom:50%;" />

The 6 orbital elements can determine an orbital. But not every orbit need 6 elements(e.g. circle orbit, equatorial orbit)

- $a$ determine the orbit size.
- $e$ determine the orbit shape.
- $\Omega, i$ determine the orbit plane orientation.
- $\omega$ determine the orbit orientation within plane.
- $\theta$ determine the SC location. $\theta= \theta(t)$.

## form orbit elements to position and velocity

### time of flight 

Kepler's work gave rise to two classes of problems. One is to find the time to travel between
two known points on an orbit, using Kepler's Equation. The other is to find a S/C future
location given the last known position and velocity vectors at time $t$, which is Kepler's
Problem or Propagation.

<img src="{{site.url}}/images/the-control-of-space-craft/image-20230923161141914.png" alt="image-20230923161141914" style="zoom:50%;" />

In order to simplify the problem, we introduced $E$, the eccentric anomaly in radians, and $M=E-e\sin E$, the mean anomaly. We define two times: $t_p$ for the time that SC passes periapsis, and $t$ for any time.

From the elliptical geometry, we have 
$$
1+e\cos \theta=\frac{1-e^2}{1-e\cos E}\\
\tan^2\frac{\theta}2=\frac{1+e}{1-e}\tan^2\frac E2
$$
After some basic integral operation, we have
$$
t-t_p=\sqrt{\frac{a^3}{\mu}}(E-e\sin E)
$$
Let $E=2\pi$, we can get the period of the orbit, and the average circle velocity of the orbit:
$$
T=2\pi\sqrt\frac {a^3} \mu\\
n=\sqrt\frac {a^3} \mu
$$
When we get the average velocity, it is easy to get $M$
$$
M=n(t-t_p)=\sqrt\frac {a^3} \mu(t-t_p)=E-e\sin E
$$
The equation gives us a way to calculate $E$, when given $a, e,t$. Further more, $\theta$ is given by $\tan^2\frac{\theta}2=\frac{1+e}{1-e}\tan^2\frac E2$.One  $\theta$  corresponds with one $|\vec r|$, which indicates the position. 

Because $\vec H=\vec r\times \vec v$ is a constant vector, it is easy to calculate $\vec v$

## example

Q: A SC in Kepler orbit with $a=10000\text{km}, e=0.2,t_p=1000s,\mu=3.986\times10^{14}\text{m}^3/\text{s}^2$. 

- It takes how long from perigee to apogee?
  $$
  T=2\pi\sqrt\frac {a^3} \mu=9952\text{s}\\
  t_0=\frac T2=4976\text{s}
  $$

- What is the $\theta$ when $r=9600\text{km}$?
  $$
  p=a(1-e^2)=9600\text{km}\\
  r=\frac{p}{1+e\cos \theta}=9600\text{km}\\
  \therefore \cos \theta=0,\theta=90\degree\text{ or }\theta=270\degree
  $$

- 

## 中国空间站轨道参数

https://www.cmse.gov.cn/gfgg/zgkjzgdcs/

2023-10-11

[进行轨道计算的代码]({{site.url}}/code/the-control-of-space-craft/orbit.py)

[使用的轨道数据]({{site.url}}/code/the-control-of-space-craft/orbit_elements.csv)