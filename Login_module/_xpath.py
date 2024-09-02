#
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located,title_is,title_contains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *

driver=webdriver.Chrome()
driver.get("D:/Testing_app/dynamic.html")
driver.maximize_window()
sleep(2)
#
# driver.find_element("xpath","//input[@id='adder1']").click()
#
# wait=WebDriverWait(driver,30)
# v=visibility_of_element_located(("xpath","//select[@id='cars1']"))
# wait.until(v)
#
# print("element is loaded and visipal in web  page")
#
# els=driver.find_element("xpath","//select[@id='cars1']")
# s=Select(els)
# s.select_by_visible_text("Audi")
#
# sleep(2)
#
#
# ###########################33
#
# driver.find_element("xpath","//input[@id='adder1']").click()
#
# try:
#     waits=WebDriverWait(driver,30)
#     sl=visibility_of_element_located(("name","Toyota"))
#     waits.until(sl)
# except TimeoutException:
#     print("element is not visibal")
#
# els=driver.find_element("xpath","//select[@id='cars2']")
# # slv=Select(els)
# els.is_displayed()
# print("it is working")


# s=['cpple','cndroid']
#
# for i in s:
#     str = ''
#     for j in i:
#         if j == 'c':
#             str+='a'
#         else:
#             str+=j
#
# print(str)

list1=list([1,2,3])

print(list1)









