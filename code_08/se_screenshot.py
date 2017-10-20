from selenium import webdriver
import time

# 访问百度
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

driver.get_screenshot_as_file('baidu_selenium.jpg')
driver.quit()
