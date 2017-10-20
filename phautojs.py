# -*- coding: utf-8 -*-  
""" 
Created on Mon May 16 16:38:00 2016 

@author: DJ 
"""


import time
from selenium import webdriver

driver = webdriver.PhantomJS(
    executable_path="G:/Python/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver.get("https://www.shanbay.com/accounts/login/")
elem_user = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[1]/input')
elem_user.send_keys('用户名')
elem_pwd = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[2]/input')
elem_pwd.send_keys('密码')
elem_sub = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[6]/button')
elem_sub.click()

time.sleep(1)
driver.get("https://www.shanbay.com/team/team/")
elem_keyword = driver.find_element_by_xpath('//*[@id="group-form"]/div/input')
elem_keyword.send_keys(u'雅思')
elem_button = driver.find_element_by_xpath('//*[@id="group-form"]/div/button')
elem_button.click()
time.sleep(1)
teams = []
for team in driver.find_elements_by_class_name('title'):
    if team.get_attribute("href") != None:
        teams.append(team.get_attribute("href"))
members = []
for team in teams[:5]:
    driver.get(team)
    for i in range(10):
        member = driver.find_element_by_xpath('//*[@id="teams_rank_table"]/tbody/tr['+str(i + 1)+']/td[2]/a')
        # //*[@id="teams_rank_table"]/tbody/tr[1]/td[2]/a
        # //*[@id=\"teams_rank_table\"]/tbody/tr[1]/td[2]/a
        members.append(member.get_attribute('href'))
bookdic = {}
for member in members:
    driver.get(member)
    bookurl = driver.find_element_by_xpath('//*[@id="my-wordbooks-heading"]/h3/small/a')
    bookurl.click()
    time.sleep(1)
    books = driver.find_elements_by_class_name('wordbook-title')
    for book in books:
        title = book.get_attribute('title')
        if title in bookdic:
            bookdic[title] = bookdic[title] + 1
        else:
            bookdic[title] = 1
retbook = sorted(bookdic.items(), key=lambda d: d[1], reverse=True)
for i in range(5):
    print(retbook[i][0])
driver.close()
