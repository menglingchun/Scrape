# coding:utf-8
# import sys
# reload(sys)
# sys.setdefaultencoding('gbk')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import json

def generateItems(url):
    url_base = 'http://car.autohome.com.cn/config/series/'
    driver = webdriver.PhantomJS()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    lis = [li for li in soup.find("div", class_="tab-content-item current").find_all("li") if li.has_attr("id")]
    items = {li['id']: [li.find("h4").get_text(), li.find("div").get_text(), url_base + li['id'].strip('s') + '.html'] for li in lis}
    return items

def fetchData(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    content = []
    changkuangao = soup.find(id="tr_4")
    changkuangao_title = changkuangao.find("th").get_text()
    zhouju = soup.find(id="tr_17")
    zhouju_title = zhouju.find("th").get_text()
    if changkuangao_title == '长*宽*高(mm)':
        changkuangao_num = changkuangao.find("td").get_text()
    else:
        changkuangao_num = None
    if zhouju_title == '轴距(mm)':
        zhouju_num = zhouju.find("td").get_text()
    else:
        zhouju_num = None

    return [changkuangao_num, zhouju_num]



t1 = time.time()

url = 'http://www.autohome.com.cn/suv/#pvareaid=103451'

items = generateItems(url)
items_json = json.dumps(items, indent=4)
print items_json
with open('itemstest.json', 'w') as f:
    f.write(items_json,)

# with open('items.json', 'r') as f:
#     items = json.load(f, 'gbk')
# for key, value in items.items():
#     value = value + fetchData(value[2])
#     print key
#     print value[0], value[1], value[2], value[3], value[4]
#     print '-' * 50


t2 = time.time()
print 'Load time with Phantom: ', (t2 - t1)*1000, 'msec'


#还没有把 暂无指导价 的车型排除！！！











# api_url = 'http://api.mall.autohome.com.cn/gethomead/110100?_appid=car'
# s = requests.Session()
# s.get('http://www.autohome.com.cn/beijing/')
# r = s.get(api_url)
# print r.content

