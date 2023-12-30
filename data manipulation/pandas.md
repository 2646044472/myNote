常见数据清洗操作
```python
pd.set_option("display.max_columns", 150)
pd.set_option("display.max_colwidth", 150)
students.dupilcated(subset=["学号","班别"])
students.isnull()
students["班别"].value_counts()
df.rename(index={})
df.rename(columns={"_2":"2","_6":"6"}, inplace="True")  #原地修改，可以是方法、函数
str.upper  #转大写
df.set_index("Name")
df.reset_index()
df.sort_index(inplace="True")  #不返回结果
df[["人口","面积"]]=df["人口密度"].str.split("/",expand=True)

```
在求average时index=0是行 index=1是列
