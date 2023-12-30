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
df.explode("课程列表")
df.fillna({"A":0,"B":10},inplace=True)  #填充缺失值
df.dropna(subset=["学号"],inplace=True)
df.drop_duplicates(subset=["姓名","班级"])
df["学校"].replace(["清华"],"清华大学")

```
在求average时index=0是行 index=1是列
