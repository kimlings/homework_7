# 作业：我们在课堂上写了一个二分法的程序，但是，但是。。如果函数是单调递增的，一切都是对的。如果是递减呢？好象就不对啦，想想为什么？
#
# 请写出一个二分法找方程根的通用函数，加到大家的软件包里去。能够处理单调递增和递减的情况。
import numpy as np
from liangyanling import func

def f(x):
    pi=3.14
    return 2*np.sin(pi*x)+ np.cos(pi*x)
#调用二分法函数，输入要求解的函数f、根所在的区间、误差范围
root,k=func.erfenfa(f,0,1,0.01)
print("root=",root,"k=",k)  #输出根和循环次数

