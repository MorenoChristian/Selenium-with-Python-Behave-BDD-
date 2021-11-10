from behave import *
from selenium import webdriver
from time import sleep

@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='C:/Users/Christian/Desktop/Platzi/Curso Selenium/Práctica/ChromeDriver/chromedriver.exe')


@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com')


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    driver = context.driver
    
    driver.find_element_by_id('txtUsername').send_keys(user)
    driver.find_element_by_id('txtPassword').send_keys(pwd)
    


@when('Click on login button')
def step_impl(context):
    login_button = context.driver.find_element_by_xpath('//*[@id="btnLogin"]')
    login_button.click()


@then('User must succesfully login to the Dashboard page')
def step_impl(context):
    '''try to find Dashboard on page'''
    text = context.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').text
    assert text == 'Dashboard'
    sleep(3)
    context.driver.quit()
