# coding: utf-8

from selenium import webdriver
from lxml import etree
import pandas as pd

# 用selenium模拟打开网页
browser = webdriver.Chrome()
browser.get('http://jishukong.com/statistics')
source = browser.page_source                  # 拿到网页源代码

# 将网页进行解析
html = etree.HTML(source)                     
trs = html.xpath('//tr[@class="ng-scope"]')
hero = []
for i,tr in enumerate(trs):                   # 获取数据
    pm = tr.xpath('td[1]/text()')[0]
    yx = tr.xpath('td[2]/a/span/text()')[0]
    wz = tr.xpath('td[3]/text()')[0]
    sl = tr.xpath('td[4]/text()')[0]
    dcl = tr.xpath('td[5]/text()')[0]
    bjl = tr.xpath('td[6]/text()')[0]
    rjsycs = tr.xpath('td[7]/text()')[0]
    js = tr.xpath('td[8]/text()')[0]
    sw = tr.xpath('td[9]/text()')[0]
    zg = tr.xpath('td[10]/text()')[0]
    cjzdls = tr.xpath('td[11]/text()')[0]
    zcyxsh = tr.xpath('td[12]/text()')[0]
    csyxsh = tr.xpath('td[13]/text()')[0]
    zzll = tr.xpath('td[14]/text()')[0]
    bds = tr.xpath('td[15]/text()')[0]
    jsdfyg = tr.xpath('td[16]/text()')[0]
    jsjfyg = tr.xpath('td[17]/text()')[0]
    jq = tr.xpath('td[18]/text()')[0]
    twzph = tr.xpath('td[19]/text()')[0]
    hero.append([pm,yx,wz,sl,dcl,bjl,rjsycs,js,sw,zg,cjzdls,zcyxsh,csyxsh,zzll,bds,jsdfyg,jsjfyg,jq,twzph])

# 数据整理
df = pd.DataFrame(hero,columns = ['排名','英雄','位置','胜率','登场率','被禁率','人均使用次数','击杀','死亡','助攻','场均最大连杀','造成英雄伤害','承受英雄伤害','总治疗量','补刀数','击杀敌方野怪','击杀己方野怪','金钱','同位置排名'])
df.to_csv('d:\\desktop\\hero.csv')
