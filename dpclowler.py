from bs4 import BeautifulSoup
import requests
import csv

# webpageのテキストを取得
r = requests.get("http://tisintecgrp-kenpo.or.jp/faq/f_fuyou/")
# webpageをパースし必要なテキストを収集
bs = BeautifulSoup(r.text, "html.parser")
qa_items = bs.find_all("div", class_="qa-faq")

with open("qa_items.csv","w", newline="", encoding="UTF-8") as file:
  writer = csv.writer(file)
  
  for index, qa_item in enumerate(qa_items):
    # QAの取得
    question = str(qa_item.find("a", class_="qa-faq-anchor").text)
    answer = str(qa_item.find("div", class_="qa-faq-answer").text)
    # trim
    question = question.replace("\n", "")
    answer = answer.replace("\n", "")
    # 出力
    # dialogplayの制約で発話例が4つは必要
    writer.writerow([index, question, answer])
    writer.writerow([index, question])
    writer.writerow([index, question])
    writer.writerow([index, question])
