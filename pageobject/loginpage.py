
from utilities._lib import seleniumwrapper
from utilities.execl_lib import *

@attach_element("loginpage")
class LoginPage:
    # logger=logGen.loggen()

    def __init__(self,driver):
        self.driver=driver
        self.wrappe=seleniumwrapper(self.driver)

    def login(self,email,password):
        # self.logger.INFO("******************* TEST LOGIN ****************")
        self.wrappe.enter_text(self.txt_email, value=email)
        self.wrappe.enter_text(self.txt_password,value=password)
        self.wrappe.click_element(self.btn_login)

        # self.logger.info("**********login complet *******")





















































