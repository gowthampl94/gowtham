from utilities._lib import seleniumwrapper
from utilities.execl_lib import attach_element


@attach_element("registrationpage")
class Registrationpage:
    # logger=logGen.loggen()

    def __init__(self,driver):
        self.driver=driver
        self.wrapper=seleniumwrapper(self.driver)


    def register(self,gender,fname,lname,email,password):
        # self.logger.info("***********rigester page ****************")
        if gender.upper() == "MALE":
            self.wrapper.click_element(self.rdo_male)
        elif gender.upper() == "FEMALE":
            self.wrapper.click_element(self.rdo_female)
        else:
            raise ValueError("Invalid Gender")

        #fname text field
        self.wrapper.enter_text(self.txt_fname, value=fname)

        #lname text field
        self.wrapper.enter_text(self.txt_lname,value=lname)

        #enter email
        self.wrapper.enter_text(self.txt_email,value=email)

        #enter password
        self.wrapper.enter_text(self.txt_password,value=password)

        #enter conform passowword
        self.wrapper.enter_text(self.txt_confirmpassword,value=password)

        #click on the register
        self.wrapper.click_element(self.btn_register)

        # self.logger.info("****************register completed *************")

        
        







