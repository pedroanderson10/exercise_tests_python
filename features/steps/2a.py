from behave import*
from selenium import webdriver
from time import sleep
import re
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


@given("a user is in the LEAD platform login page #2")
def given(context):
    context.driver = webdriver.Chrome("D:/Python Projects/testesCapacitacao/drivers/chromedriver.exe")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")

@when("the user insert his invalid credentials")
def when(context):
    context.driver.find_element_by_id("login").send_keys("leonardoalunoprod")
    context.driver.find_element_by_id("password").send_keys("abcd12345678")
    context.driver.find_element_by_id("login-btn").submit()

@then("LEAD platform returns that the credentials are not valid")
def then(context):
    #WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-login/html/body/form/div[1]")))
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-login/html/body/form/div[1]"),
                                     "Usuário e/ou senha inválidos. Verifique o usuário e senha e tente novamente."))

    context.driver.quit()



