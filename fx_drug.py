import numpy as np
data=np.loadtxt(open('D:\drugs.csv'),delimiter=',', encoding='utf8',dtype=str) #读取数据
#print(data)打印数据
a=0                 #记录行数
count=0              #记录满足条件的数量
zy=[]                #List储存满足条件的数据
dict={}            #字典储存最终统计结果
index=data[0,:][6:]  #储存中药名称，作为字典的seq
counter=[]           #储存中药数量
result=dict.fromkeys(index)
#判断是否满足某种伏邪,如果满足则提取数据存入zy[]
n=int(input("输入伏邪代码，“风\寒\湿\热\瘀\毒”分别为“0/1/2/3/4/5” ："))
for tof in data[:,n]:   
    if tof=='1':
         zy.append(data[a,:][6:])
         a=a+1
         count=count+1
    else:
         a=a+1
#统计每种药材的数量
sum=0
j=0
for i in range(len(result)):
    sum=0
    for j in zy:
        if j[i] =='1':
            sum=sum+1
    counter.append(sum)
num=0
for key  in  result:
    result[key]=counter[num]
    num=num+1
print(result)
