plt不支持df只支持Series,只有sns才支持df
绘制图表常见操作：
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 绘制折线图
sns.lineplot(x='timepoint', y='signal', data=data)
# 绘制散点图
sns.scatterplot(x='sepal_length', y='sepal_width', data=data)
# 绘制条形图
sns.barplot(x='day', y='total_bill', data=data, estimator=np.max)
# 绘制直方图
sns.histplot(data['total_bill'])
# 绘制小提琴图
sns.violinplot(x='day', y='total_bill', data=data)
# 绘制计数图
sns.countplot(x='class', data=data)
# 绘制热力图
sns.heatmap(data, annot=True ) 
# 绘制饼图
plt.pie(sizes, labels=labels, colors=colors, autopct='%.1f%%')  #%表示文字开头, %%表示%

plt.show()  #可以一同展示多个图 

#可以传入colour=参数，或者使用sns.set_paletee("crest")来调色
#传入hue=参数来分类调色,ig. hue="species",引入分类变量
#传入size=参数来改变点大小
#图例太长挡住元素时：plt.legend(bbox_to_anchor=(1, 1))，此时0,1表示位置

#绘制多个图时:
#可以传入binwidth=0.1, 当同时展示多个图时统一宽度,并用label=""备注标签
#记得plt.legend()
#对比小提琴图时传入x="",y="",这样图不会挤到一起
fig, axes = plt.subpolts(1,3,figsize=(15,5)) #一行三列空白子图,绘图时再传入ax=axes[0]
sns.piarplot(df) #一共得到n*n个图,一次性探索变量分布
 
```
