
from utilities._lib import seleniumwrapper
from utilities.execl_lib import attach_element


@attach_element("homepage")
class HomePage:
    # logger=logGen.loggen()


    def __init__(self,driver):
        self.driver=driver
        self.wrapper=seleniumwrapper(self.driver)

    def click_login(self):
        self.wrapper.click_element(self.lnk_login)

    def click_register(self):
        self.wrapper.click_element(self.lnk_register)

    def click_books(self):
        self.wrapper.click_element(self.btn_books)
        






















































