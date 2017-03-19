# encoding: utf-8

from selenium import webdriver
import urllib

browser = webdriver.Chrome()
browser.set_page_load_timeout(10)

url = 'http://www.17huo.com/?mod=search&code=main&cid=0&market=0&keyword=%E7%BE%8A%E6%AF%9B&sq=2&page=1'
browser.get(url)
items = browser.find_elements_by_css_selector('body > div.wrap > div:nth-child(2) > div.p_main > ul > li')
for item in items:
    title = item.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)').text
    price = item.find_element_by_css_selector('div > a > span').text
    print(title + ': ' + price)