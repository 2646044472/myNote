请下载Edge浏览器驱动：https://msedgedriver.azureedge.net/120.0.2210.91/edgedriver_win64.zip  

把下载好的文件添加到Path



准备
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
wd = webdriver.Edge()
```

find_element(s)方法：
By.ID,  By.CLASS_NAME,  By.TAG_NAME,  By.CSS_SELECTOR
```python
wd.get("https://www.umeh.top/course/GEGA1006")
# elements = wd.find_element(By.CLASS_NAME, 'break-words')
# elements = wd.find_element(By.TAG_NAME, 'div')
```

一些重要的get_attribute:
```python
element.get_attribute('textContent')
element.get_attribute('class')    # 获取class的值
element.get_attribute('outerHTML')
```
