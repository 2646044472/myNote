```python
import requests
from bs4 import BeautifulSoup

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=head)
    soup = BeautifulSoup(response.text, "html.parser")
    all_title = soup.findAll("span", attrs={"class": "title"})
    for title in all_title:
        title_string = title.string
        if title_string[1] != '/':
            print(title_string)
```
