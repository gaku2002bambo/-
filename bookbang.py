#python3 bookbang.py

from bs4 import BeautifulSoup
import requests
import pandas


url="https://www.bookbang.jp/ranking-book-review"#{}でページが変更される部分を記述

r = requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")

contents=soup.find_all('div',class_='text')
links=soup.find_all('a',class_='clr')[0:20]

linklist=[]
for link in links:
  linklist.append(link.get("href"))

pricelist=[]
summarylist=[]

for link in linklist:
  res=requests.get('https://www.bookbang.jp'+link)
  soup=BeautifulSoup(res.text,'html.parser')

  #価格を取得
  infos=soup.find('dl',class_='books_info')
  moreinfos=infos.find_all('dd')
  moreinfos2=[s.text for s in moreinfos]
  price=[s for s in moreinfos2 if '円'in s]
  if not price:
    price2='価格が表示されていません'
  else:
    price2=price[0]
  pricelist.append(price2)
  #内容紹介を取得
  summary=soup.find('div',class_='introduction').text
  summarylist.append(summary)

list_book=[]
for i in range(0,20):
  list_book.append({'title':contents[i].text,'price':pricelist[i],'summary':summarylist[i]})


#csvに保存
df=pandas.DataFrame(list_book)
df.to_csv('books.csv',encoding='utf-8-sig')