import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

titleList = []

for j in range(1,100, 20):

    res = req.get("https://search.naver.com/search.naver?sm=tab_sug.top&where=news&ssc=tab.news.all&query=%EC%86%8D%EB%B3%B4&oquery=%EC%86%8D%EB%B3%B4&tqi=i8eexlqosesss4i9qhsssssstis-252461&acq=%EC%86%8D%EB%B3%B4&acr="+str(j))
    soup = bs(res.text,"lxml")
    title = soup.select("a.news_tit")
    for i in title :
        titleList.append(i.text)

dic ={"뉴스제목" : titleList}
df = pd.DataFrame(dic)
df.to_csv("data.csv", encoding="euc-kr",index=False)

