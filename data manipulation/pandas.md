常见数据清洗操作
```python
pd.set_option("display.max_columns", 150)
pd.set_option("display.max_colwidth", 150)
students.dupilcated(subset=["学号", "班别"])
students.isnull()
students["班别"].value_counts()
df.rename(index={})
df.rename(columns={"_2": "2", "_6": "6"}, inplace=True)  # 原地修改，可以是方法、函数
str.upper  # 转大写
df.set_index("Name")
df.reset_index()
df.sort_index(inplace=True)  # 不返回结果
df[["人口", "面积"]] = df["人口密度"].str.split("/", expand=True)
df = df.drop("人口秘密", axis=1)
df["姓"].str.cat(df["名"],sep="-")
pd.melt(df, id_vars=['国家代码','年份'], var_name='年龄组'， value_name='肺结核病例数')  #转换除了国家代码、年份外的变成一列年龄组
df.explode("课程列表")    #df['genres'] = df['genres'].apply(eval)注意转换字符串，看清楚是字符串还是列表
df.fillna({"A":0,"B":10},inplace=True)  #填充缺失值
df.dropna(subset=["学号"],inplace=True)
df.drop_duplicates(subset=["姓名","班级"])
df["学校"].replace(["清华"],"清华大学")
pd.concat([df1,df2], ignore_index=True, axix=0)
pd.merge(df1,df2, on='ID')  #可以调用ledt_on, right_on去对应, 调用suffiex=['_df1','_df2']在合并时添加后缀,调用how="inner","outer","left","right"决定保留值
df.groupby("分店编号")
df.groupby(["分店编号","时间段"])[["销售额","销售数量"]].mean()   #有内层索引和外层索引
pd.pivot_table(df, index=["分点编号","时间段"], columns="商品类别", values="销售额", aggfunc=np.sum)  #默认是求平均
age_bins=[0,10,20,30,40,50,60,100]
age_labels=["儿童","青少年","青年","壮年","中年","中老年","老年"]
pd.cut(df["年龄"], age_bins, label=age_lables)
df.reset_index()  #group_by后出现外层索引时重置索引 
df.query('(性别 == "男")&("年龄 < 20")')  #快速查询
```
在求average时index=0是行 index=1是列
