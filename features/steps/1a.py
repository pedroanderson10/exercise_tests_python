from behave import*
from selenium import webdriver
from time import sleep
import re
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions

@given("a user is in the LEAD platform login page")
def given(context):
    context.driver = webdriver.Chrome("D:/Python Projects/testesCapacitacao/drivers/chromedriver.exe")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")

@when("the user insert his valid credentials")
def when(context):
    context.driver.find_element_by_id("login").send_keys("leonardoalunoprod")
    context.driver.find_element_by_id("password").send_keys("abcd1234")
    context.driver.find_element_by_id("login-btn").submit()

@then("LEAD platform redirects the user to the home page")
def then(context):
    WebDriverWait(context.driver, 15).until(expected_conditions.visibility_of_element_located((By.ID, "smallHeader")))
    context.driver.quit()
    #WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.ID, "smallHeader")))
    #wait = WebDriverWait(context.driver, 10)
    #wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))
    #sleep(10)
    #context.driver.find_element_by_id("smallHeader").contains("My Courses")
    #context.driver.getPageSource().contains("My Courses")

