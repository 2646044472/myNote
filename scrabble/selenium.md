请下载Edge浏览器驱动：https://msedgedriver.azureedge.net/120.0.2210.91/edgedriver_win64.zip  

把下载好的文件添加到Path

1.  wd.find_element(By.ID, 'username').send_keys('byhy')
2.  wd.find_element(By.CLASS_NAME, 'password').send_keys('sdfsdf')
3.  wd.find_element(By.TAG_NAME, 'input').send_keys('sdfsdf')
4.  wd.find_element(By.CSS_SELECTOR,'button[type=submit]').click()

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
wd = webdriver.Edge()
wd.get("https://www.umeh.top/course/GEGA1006")
# elements = wd.find_element(By.CLASS_NAME, 'break-words')
elements = wd.find_element(By.TAG_NAME, 'div')
print(elements.text)
```

