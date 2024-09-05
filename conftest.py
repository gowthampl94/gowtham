from selenium.webdriver.chrome.webdriver import WebDriver as chrome
from selenium.webdriver.firefox.webdriver import WebDriver as firefox
from selenium.webdriver.edge.webdriver import WebDriver as edge
from pytest import fixture
from selenium.webdriver.chrome.options import Options as chromeoptions
from selenium.webdriver.firefox.options import Options as firefoxoptions
from selenium.webdriver.edge.options import Options as edgeoptions
from pageobject.loginpage import LoginPage
from pageobject.registerpage import Registrationpage
from pageobject.homepage import HomePage
from pageobject.bookpage import Bookpage
from copy import deepcopy


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", dest="browser")
    parser.addoption("--env", action="store", default="test", dest="env")
    parser.addoption("--headless", action="store_true", dest="headless", default=False)


@fixture
def _config(request):

    class Testconfigeration:
        url = "https://demowebshop.tricentis.com/"
        email="steve_jobs@gmail.com"
        password="password123"

    class Stagconfigeration:
        url = "https://demowebshop.tricentis.com/"
        email = "steve_jobs@gmail.com"
        password = "password123"

    exe_env=request.config.option.env

    if exe_env.upper() == "TEST":
        print("Excution environment is TEST")
        return Testconfigeration()
    elif exe_env.upper() == "STAGE":
        print("Excution environment is STAGE")
        return Stagconfigeration()
    else:
        raise Exception("invalid excution environment")
@fixture
def driver(request,_config):
    borwser_name=request.config.option.browser
    is_headless=request.config.option.headless
    options=None
    print("excuting setup from driver method")
    if borwser_name.upper() == "CHROME":
        if is_headless:
            options=chromeoptions()
            options.add_argument("--headless=new")
        _driver=chrome(options=options)
    elif borwser_name.upper() == "FIREFOX":
        if is_headless:
            options=firefoxoptions()
            options.add_argument("--headless")
        _driver=firefox(options=options)
    elif borwser_name.upper() == "EDGE":
        if is_headless:
            options=edgeoptions()
            options.add_argument("--headless-new")
        _driver=edge(options=options)
    else:
        raise Exception("invalid browser")
    _driver.get(_config.url)
    _driver.maximize_window()
    yield _driver
    print("Excuting teardown")
    _driver.quit()

@fixture
def pages(driver):
    class pages:
        homepage = HomePage(driver)
        loginpage = LoginPage(driver)
        registationpage=Registrationpage(driver)
        bookpage= Bookpage(driver)

    return pages()




































