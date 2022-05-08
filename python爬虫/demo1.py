import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lxml import etree


web = webdriver.Chrome()
web.get('http://auto.neepu.edu.cn/info/1223/2298.htm')
page = web.page_source
html = etree.HTML(page)
tr = html.xpath('//tbody/tr')
for i in tr:
    text = i.xpath('./td/p/text()')
    print(text)
    print('*'*100)