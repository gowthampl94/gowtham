# from selenium import webdriver
# import select
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located,title_is
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
#
# # driver=WebDriver()
# # sleep(2)
# # # driver.get("https://www.shoppersstack.com/")
# # driver.get("https://www.python.org/downloads/")
# # # driver.get("http://demowebshop.tricentis.com/books")
# # # driver.get("C:/Users/Gowtham p/OneDrive/Documents/Downloads/demo.html")
# # sleep(2)
# # driver.maximize_window()
# # sleep(5)
# # # work python python 3.8.19
# # element=driver.find_element("xpath","//a[text()='Python 3.8.19']/../..//a[text()='Release Notes']")
# # element.click()
#
#
#
# # work demowebshop
# # books=["Health Book","Computing and Internet","Fiction"]
# # for book in books:
# #     _xpath=f"//a[text()='{book}']/../..//input[@value='Add to cart']"
# #     driver.find_element("xpath",_xpath).click()
# # sleep(20)
#
# # items={
# #     "Build your own cheap computer":900,
# #     "Build your own computer": 1200,
# #     "Build your own expensive computer":
# # }
# #
#
#
#
#
#
# ####################################
# # # ex :using this we click on all the check box   #call it as dynamic webelement
# # elements=driver.find_elements("xpath","//td[text()='Perl']/../..//input[@type='checkbox']")
# # for item in elements[::2]:
# #     item.click()
# # titles=driver.title
# # print(titles)
# # sleep(20)
#
# # ex 1:  it is working
#
#
# # langauges=["Python","Java","Swift","C++","Perl","JavaScript","C#"]
# #
# # for langauge in langauges:
# #     _xpath=f"//td[text()='{langauge}']/..//input[@name='download']"
# #     driver.find_element("xpath",_xpath).click()
#
#
#
# # not working
# # element=driver.find_elements("link_text","Download")
# # print(element)
# # for item in element:
# #     item.click()
# #     sleep(5)
#
#
# #
#
#
# ###########################################################################################
#
# # driver.find_element("xpath","//td[text()='Android']/..//a[text()='Download']").click()
# #
# # wait=WebDriverWait(driver,10)
# # wait.until()  #here it is asking the element name
# # driver.find_element("xpath","//td[text()='Android']/..//a[text()='Download']").click()
#
# # sleep(20)
#
# # delay=WebDriverWait(driver,10)
# # delay.until()
#
# # alert=Alert(driver)
# # alert.accept()
# # sleep(5)
#
#
# # element=driver.find_elements("xpath","//select[@id='multiple_cars']/.//option[text()='Select car:']")
# # s=Select(element)
# # s.select_by_visible_text("Audi")
# # # s.select_by_visible_text("Ford")
#
#
#
# # handl=driver.window_handles
# # driver.switch_to.window(handl[1])
#
# # opt = webdriver.ChromeOptions()
# # opt.add_experimental_option("detach",True)
# # driver = webdriver.Chrome(options=opt)
# # driver.get("C:/Users/Gowtham p/OneDrive/Documents/Downloads/demo.html")
# # sleep(2)
# # driver.maximize_window()
# # ele = driver.find_element("id","multiple_cars")
# # select_obj = Select(ele)
# # select_obj.select_by_visible_text("Audi")
# # select_obj.select_by_visible_text("BMW")
#
# # # shallow copy
# # nums = [2, 8, 5, 7, 3, 1, 9]
# #
#
#
#
#
s='1,2,3,4,5,6'
#'623451'
p=[]
r=s.split()
for i in r:
    if i == r[0]:
        p+=r[-1]
    elif i==r[-1]:
           p+=r[0]
    else:
        p+=i

print(*p)


# print(r)













# elements = []
# element = ""
# for char in s:
#     if char == ',':
#         elements.append(element)
#         element = ""
#     else:
#         element += char
# elements.append(element)
# print(element)



#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
