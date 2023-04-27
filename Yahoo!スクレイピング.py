import requests
from bs4 import BeautifulSoup
import re

#Yahoo!ニュースのトップページ情報を取得
URL="https://news.yahoo.co.jp/"
rest=requests.get(URL)

#BeatutifulSoupにYahoo!ニュースのページを読ませる
soup=BeautifulSoup(rest.text,"html.parser")

#Yahoo!ニュースの見出しとURLの情報を取得して出力する
data_list=soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
for data in data_list:
  print(data)
  print(data.text)
  print(data.attrs["href"])

