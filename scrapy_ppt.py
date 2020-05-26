# -*- coding: utf-8 -*-
"""
Created on 2020/05/26
本程式為參考網路文章的練習實作
參考的網址：https://medium.com/%E8%AA%A4%E9%97%96%E6%95%B8%E6%93%9A%E5%8F%A2%E6%9E%97%E7%9A%84%E5%95%86%E7%AE%A1%E4%BA%BAzino/python%E6%89%8B%E6%8A%8A%E6%89%8B%E7%88%AC%E5%8F%96-ppt-%E5%85%AB%E5%8D%A6%E7%89%88%E6%9C%80%E6%96%B0%E8%A9%B1%E9%A1%8C-%E5%90%AB%E5%BD%B1%E7%89%87%E8%88%87%E7%A8%8B%E5%BC%8F%E7%A2%BC-a8216873a9d3

"""

# 導入 模組(module)
import bs4
import requests

# 把 到 ptt 八卦版 網址存到URL 變數中
URL = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 設定Header與Cookie
my_headers = {'cookie': 'over18=1;'}
# 發送get 請求 到 ptt 八卦版
response = requests.get(URL, headers=my_headers)
# 印出回傳網頁程式碼
# print(response.text)


# 導入 BeautifulSoup 模組(module)：解析HTML 語法工具

# 2-1 把網頁程式碼(HTML) 丟入 bs4模組分析
soup = bs4.BeautifulSoup(response.text, "html.parser")

# 2-2 查找所有html 元素 過濾出 標籤名稱為 'div' 同時class為 title
titles = soup.find_all('div', 'title')

# 2-3 萃取文字出來。
# 因為我們有多個Tags存放在 List titles中。
# 所以需要使用for 迴圈將逐筆將List
for t in titles:
    print(t.text)
