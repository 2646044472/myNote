请下载Edge浏览器驱动：https://msedgedriver.azureedge.net/120.0.2210.91/edgedriver_win64.zip  

把下载好的文件添加到Path

测试用例：https://cdn2.byhy.net/files/selenium/sample1.html

准备
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
wd = webdriver.Edge()
wd.implicitly_wait(5)
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
element.get_attribute('outerHTML')    
element.get_attribute('value')
```

CSS selecter:
```python
elements = wd.find_elements(By.CSS_SELECTOR, '.plant')  # 如果是'plant'就等价于<plant>  .是根据class..
elements = wd.find_elements(By.CSS_SELECTOR, '#searchtext')  # '#'是id
#子元素和后代元素
elements = wd.find_elements(By.CSS_SELECTOR, '#ok > .plant > .animal')  #要求直接子元素
elements = wd.find_elements(By.CSS_SELECTOR, '#ok  .plant')  #只要是 class:plant 是 id:ok 后代就行
#可以用这个[]
elements = wd.find_elements(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')
#是div[class='SKnet'] 不是div[.SKnet]
# *是包含 ^是开头 $是结尾  如：[href*="miitbeian"]
#可以用F12的element验证css
# ,优先级低 #t1>span,p 是找 #t1>span 和 p 别乱用()
#第n个子元素 #t1 :nth-child(2) 倒数元素:nth-last-child(2)
#同类型的第n个子元素0 span:nth-of-type(1)
#兄弟节点 +是紧跟节点 ~是后面所有兄弟节点
```
