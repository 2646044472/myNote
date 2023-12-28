请下载Edge浏览器驱动：https://msedgedriver.azureedge.net/120.0.2210.91/edgedriver_win64.zip  

把下载好的文件添加到Path

测试用例：https://cdn2.byhy.net/files/selenium/sample1.html

准备
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
wd = webdriver.Edge()
```

find_element(s)方法：
```python
wd.get("https://www.umeh.top/course/GEGA1006")
# By.ID,  By.CLASS_NAME,  By.TAG_NAME,  By.CSS_SELECTOR
elements = wd.find_element(By.CLASS_NAME, 'break-words')
elements = wd.find_element(By.TAG_NAME, 'div')
```

一些重要的get_attribute:
```python
element.get_attribute('textContent')
element.get_attribute('class')    # 获取class的值
element.get_attribute('outerHTML')    #非常强大
element.get_attribute('value')
```

CSS selecter:
```python
elements = wd.find_elements(By.CSS_SELECTOR, '.plant')  # 如果是'plant'就等价于<plant>  .是根据class..
elements = wd.find_elements(By.CSS_SELECTOR, '#searchtext')  # '#'是id
#子元素和后代元素
elements = wd.find_elements(By.CSS_SELECTOR, '#ok > .plant > .animal')  #要求直接子元素
elements = wd.find_elements(By.CSS_SELECTOR, '#ok  .plant')  #只要是 class:plant 是 id:ok 后代就行

```
