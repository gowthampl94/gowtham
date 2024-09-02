
from utilities._lib import seleniumwrapper
from utilities.execl_lib import attach_element

@attach_element("books")
class Bookpage:

    def __init__(self,driver):
        self.driver=driver
        self.wrepper=seleniumwrapper(self.driver)

    def book(self, fname, lname,email, company, city, address1, address2, pin_code, phone, address,dropdown):

        #click on the booke image
        self.wrepper.click_element(self.Btn_image)

        #click on the adda to cart
        self.wrepper.click_element(self.btn_addcart)

        #click on the shoppercart
        self.wrepper.click_element(self.lnk_txt_shoppercart)

        #click on the i agree radio button
        self.wrepper.click_element(self.checkbox_iagree)

        #click on the chick checkout
        self.wrepper.click_element(self.btn_chickout)

        #click on the billing address   select new address
        self.wrepper.select_element(self.option_newaddres,address)

        #enter the fname
        self.wrepper.enter_text(self.txt_fname, value=fname)

        #enter the lname
        self.wrepper.enter_text(self.txt_lname, value=lname)

        #enter the email
        self.wrepper.enter_text(self.txt_email, value=email)

        #enter the company
        self.wrepper.enter_text(self.txt_company, value=company)

        #contry drop down
        self.wrepper.select_element(self.txt_dropdown_canada, dropdown)

        #enter the city
        self.wrepper.enter_text(self.txt_city, value=city )

        #enter the address1
        self.wrepper.enter_text(self.txt_address1, value=address1)

        #enter the address2
        self.wrepper.enter_text(self.txt_address2, value=address2)

        #enter the zip code
        self.wrepper.enter_text(self.txt_zipcode, value=pin_code)

        #enter the txt_phoneno
        self.wrepper.enter_text(self.txt_phonenum , value=phone)

        #enter the faxnumver
        self.wrepper.enter_text(self.txt_fxnumber, value=phone)

        #click on continue
        self.wrepper.click_element(self.btn_bill_add_cintinue)

        # click on the  drop down
        self.wrepper.select_element(self.option_second_shopp)



res=Bookpage()























