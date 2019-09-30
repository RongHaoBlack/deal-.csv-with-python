# deal-.csv-with-python

import numpy as np
from collections import Counter
data=np.loadtxt(open('D:\sta.csv'),delimiter=',',skiprows = 1, encoding='utf8',dtype=str) #读取数据
n=int(input("输入伏邪代码，“风\寒\湿\热\瘀\毒”分别为“0/1/3/5/6/7” ："))
a=0#记录行数
count=0#记录满足条件的数量
fangji=[]  #储存满足条件的数据
for tof in data[:,n]:   #判断是否满足某种伏邪
     if tof=='1':
        fangji.append(data[a,8])
        a=a+1
        count=count+1
     else:
            a=a+1
print("符合条件的数据有：%d"%count)
Result=Counter(fangji)
print("结果为",Result)
