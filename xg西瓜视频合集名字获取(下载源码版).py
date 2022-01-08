from bs4 import BeautifulSoup



with open ('./网页源码.html','r',encoding='UTF-8',errors='ignore') as 源文件变量:
        源文件数据=源文件变量.read()
bs4解析出来的数据 = BeautifulSoup(源文件数据, "html.parser")



筛选后的数据=bs4解析出来的数据.select('div.HorizontalFeedCard.projection_seriesItem > div.HorizontalFeedCard__contentWrapper > div.HorizontalFeedCard__rich__media > a.HorizontalFeedCard__title.color-link-content-primary >  span')
print(筛选后的数据)

 
