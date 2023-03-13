import requests
from bs4 import BeautifulSoup

# 发送请求
url = input("请输入你要获取的网页:")
response = requests.get(url)

# 解析HTML
soup = BeautifulSoup(response.content, 'html.parser')
meta_tag = soup.find("meta", {"name":"description"})


# description = meta_tag["content"]
# print(description)


if meta_tag:
    description = meta_tag["content"]
    print(description)
else:
    print("该网页没有description信息.")






