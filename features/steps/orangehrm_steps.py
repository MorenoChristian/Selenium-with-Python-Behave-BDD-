from behave import Given, When, Then
from selenium import webdriver

@Given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path='C:/Users/Christian/Desktop/Platzi/Curso Selenium/Práctica/ChromeDriver/chromedriver.exe')


@When('open orange hrm homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com')

@Then('verify that the logo present on page')
def VerifyLogo(context):
    status = context.driver.find_element_by_xpath('//*[@id="divLogo"]/img').is_displayed()
    assert status is True, 'The logo is not displayed'

@Then('close browser')
def CloseBrowser(context):
    context.driver.quit()