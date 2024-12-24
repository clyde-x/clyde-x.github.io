import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
from datetime import datetime
from scipy.spatial.transform import Rotation as R


def vec_angle(a, b):  # 计算两个向量的夹角
    a_ = np.sqrt(np.dot(a, a))
    b_ = np.sqrt(np.dot(b, b))
    return np.arccos(np.dot(a, b) / (a_ * b_))


class Orbit():
    def __init__(self, ome):
        self.mu = 3.986004418e14
        self.ome = ome
        self.time = ome[0]
        self.x = ome[1] * 1000
        self.y = ome[2] * 1000
        self.z = ome[3] * 1000
        self.vx = ome[4] * 1000
        self.vy = ome[5] * 1000
        self.vz = ome[6] * 1000

    def get_orbit_elements(self):
        self.r = np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)  # 位置大小
        self.v = np.sqrt(self.vx ** 2 + self.vy ** 2 + self.vz ** 2)  # 速度大小
        self.r_vec = np.array([self.x, self.y, self.z])  # 位置向量
        self.v_vec = np.array([self.vx, self.vy, self.vz])  # 速度向量
        self.energy = 0.5 * self.v ** 2 - self.mu / self.r  # 能量
        self.a = -self.mu / (2 * self.energy)  # 半长轴
        self.H_vec = np.cross(self.r_vec, self.v_vec)  # 角动量
        self.H = np.sqrt(self.H_vec[0] ** 2 + self.H_vec[1] ** 2 + self.H_vec[2] ** 2)  # 角动量大小
        self.p = self.H ** 2 / self.mu  # 半通径
        self.e = np.sqrt(1 - self.p / self.a)  # 离心率
        self.i = np.arccos(self.H_vec[2] / self.H)  # 倾角i
        self.b_vec = np.array([-self.H_vec[1], self.H_vec[0], 0])  # 升交点矢量
        self.e_vec = np.cross(self.v_vec, self.H_vec) / self.mu - self.r_vec / self.r  # 偏心率矢量
        self.Omega = np.arctan2(self.H_vec[0], -self.H_vec[1])  # 升交点赤经Omega
        self.omega = vec_angle(self.b_vec, self.e_vec)  # 近心点幅角omega
        if self.e_vec[2] < 0:
            self.omega = 2 * np.pi - self.omega
        self.u = vec_angle(self.b_vec, self.r_vec)  # 纬度辐角u
        if self.r_vec[2] < 0:
            self.u = 2 * np.pi - self.u
        # self.theta=np.arctan2(self.r_vec[2],np.sqrt(self.r_vec[0]**2+self.r_vec[1]**2))#真近点角theta
        self.theta = self.u - self.omega
        self.E=2*np.arctan(np.sqrt((1-self.e)/(1+self.e))*np.tan(self.theta/2))#偏近点角E
        self.M=self.E-self.e*np.sin(self.E)#平近点角M
        self.T=2*np.pi*np.sqrt(self.a**3/self.mu)#周期T
        self.tp=datetime.fromtimestamp(datetime.timestamp(self.time)-(self.M*self.T/(2*np.pi)))#近地点时间tp
        return [self.time, self.a, self.e, self.i, self.Omega, self.omega, self.theta, self.tp]

class Orbit2():
    def __init__(self,elements):
        self.time=elements[0]
        self.a=elements[1]
        self.e=elements[2]
        self.i=elements[3]
        self.Omega=elements[4]
        self.omega=elements[5]
        self.theta=elements[6]
        self.tp=elements[7]
        self.mu=3.986004418e14

    def get_v(self,plot_E=False):
        self.p=self.a*(1-self.e**2)
        self.T=2*np.pi*np.sqrt(self.a**3/self.mu)
        self.M=2*np.pi*(datetime.timestamp(self.time)-datetime.timestamp(self.tp))/self.T
        #迭代求解M=E-e*sin(E)
        self.E_list=[self.M]
        self.E=self.M
        while True:
            self.E_=self.E
            self.E_list.append(self.E)
            self.E=self.M+self.e*np.sin(self.E)
            if abs(self.E-self.E_)<1e-8:
                break
        if plot_E:
            plt.plot(self.E_list)
            plt.show()
        self.theta=2*np.arctan(np.sqrt((1+self.e)/(1-self.e))*np.tan(self.E/2))
        self.r=self.p/(1+self.e*np.cos(self.theta))
        self.vu=np.sqrt(self.mu/self.p)*(1+self.e*np.cos(self.theta))
        self.vr=np.sqrt(self.mu/self.p)*self.e*np.sin(self.theta)
        self.v=np.sqrt(self.vu**2+self.vr**2)
        return [self.v,self.vu,self.vr]

    def Loi(self):
        r = R.from_euler('zxz', [self.Omega,self.i,self.omega+self.theta])
        return r.as_matrix()

    def r_and_v(self):
        self.get_v(plot_E=True)
        self.r_o=np.array([self.r,0,0])
        self.v_o=np.array([self.vr,self.vu,0])
        self.r_i=np.dot(self.Loi().transpose(),self.r_o)
        self.v_i=np.dot(self.Loi().transpose(),self.v_o)
        return np.array([self.r_i/1000,self.v_i/1000]).reshape(6).tolist()



def read_data(file):
    data = pd.read_csv(file, names=['time', 'x', 'y', 'z', 'vx', 'vy', 'vz'])
    data['time'] = pd.to_datetime(data['time'], format="%Y-%m-%dT%H:%M:%S")
    return data

def orbit_elements(data):
    df=pd.DataFrame(columns=['time','a','e','i','Omega','omega','theta','tp'])
    for i in range(len(data)):
        orbit=Orbit(data.iloc[i])
        df.loc[i]=orbit.get_orbit_elements()
    return df

def compare(a,b):
    a=np.abs(np.array(a))
    b=np.abs(np.array(b))
    error=np.sqrt((a-b)**2)
    return error, (error/a).sum()/6

def main():
    #原始文件经过一定处理，去掉了开始的标题部分，元数据区部分，并改为逗号分隔的csv文件
    file_root = "F:\\buaa\\航天器控制原理"
    data = read_data(os.path.join(file_root, "data.csv"))
    print(data.head())

    #生成各个时刻的轨道参数文件
    # orbit_element=orbit_elements(data)
    # print(orbit_element.head())
    # orbit_element.to_csv(os.path.join(file_root, "orbit_elements.csv"), index=False)

    # 测试
    num=100
    data0 = data.iloc[num:num + 1]
    orbit_element = orbit_elements(data0)
    # print(orbit_element)
    orbit = Orbit2(orbit_element.values.tolist()[0])

    print('原始数据：')
    print(data0.iloc[0].values.tolist()[1:])
    print('通过轨道参数求出来的数据：')
    print(orbit.r_and_v())
    print('误差：')
    print(compare(data0.iloc[0].values.tolist()[1:],orbit.r_and_v()))


if __name__ == '__main__':
    main()
