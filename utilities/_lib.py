
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import logging
from typing import Self
from time import sleep
from selenium.webdriver.common.keys import Keys




MAX_TIMEOUT=10
def _wait(func):
    def wrapper(instance:Self,locater:tuple[str,str],**kwargs:dict[str,str]):
        print(f"Waiting for the element{locater}")
        element=WebDriverWait(instance.driver,MAX_TIMEOUT)
        visible=visibility_of_element_located(locater)
        element.until(visible)
        func(instance,locater,**kwargs)
    return wrapper

def __wait(cls):
    for key,value in cls.__dict__.items():
        if callable(value) and key != "__init__":
            setattr(cls,key,_wait(value))
        return cls

@__wait
class seleniumwrapper:


    def __init__(self,driver):
        self.driver=driver

    def enter_text(self,locater:tuple[str,str],*,value:str):
        self.driver.find_element(*locater).send_keys(value)

    def click_element(self,locater:tuple[str,str]):
        self.driver.find_element(*locater).click()

    def select_element(self,locater:tuple[str,str],item:str):
        element=self.driver.find_element(*locater)
        select=Select(element)
        select.select_by_index(2)
        sleep(2)


    def move_to_element(self,locater:tuple[str,str]):
        elements=self.driver.find_element(locater)
        action=ActionChains(self.driver)
        action.move_to_element(elements).perform()


    # def pagedown(self,locator:tuple[str,str],times=1):
    #    body= self.driver.find_element(locator)
    #    for _ in range(times):
    #        body .send_key(Keys.PAGE_DOWN)


    # def scroll_by(self,locator:tuple[str,str]):


class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r"C:\Users\Gowtham p\PycharmProjects\pythonProject2\shoppersstack\logs\automation_logs",
                                format='%(asctime)s:%(levelname)s:%(message)s',
                                datefmt='%m/%d/%y %I:%M:%S:%P')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
























