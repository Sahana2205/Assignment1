
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_data import data
import pytest
import time

class Test_Sahana:
    url = "https://opensource-demo.orangehrmlive.com"


    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    # def test_login(self,booting_function):
    #     self.driver.get(self.url)
    #     time.sleep(5)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_username).send_keys(data.Sahana_Data.username)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_password).send_keys(data.Sahana_Data.password)
    #     self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.login_xpath).click()
    #     print("Login Successful # {username} and {password}".format(username=data.Sahana_Data.username, password=data.Sahana_Data.password))

    # def test_invalid_login(self,booting_function):
    #     self.driver.get(self.url)
    #     time.sleep(5)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_invalid_username).send_keys(data.Sahana_Data.invalid_username)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_invalid_password).send_keys(data.Sahana_Data.invalid_password)
    #     self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.login_xpath).click()
    #     print("Login failed - INVALID CREDENTIALS")


    # def test_add_new_employee(self,booting_function):
    #     self.driver.get(self.url)
    #     time.sleep(5)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_username).send_keys(data.Sahana_Data.username)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_password).send_keys(data.Sahana_Data.password)
    #     self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.login_xpath).click()
    #     time.sleep(3)
    #     self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.pim_xpath).click()
    #     time.sleep(3)
    #     self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.add_xpath).click()
    #     time.sleep(3)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_firstname).send_keys(data.Sahana_Data.firstname)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_middlename).send_keys(data.Sahana_Data.middlename)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_lastname).send_keys(data.Sahana_Data.lastname)
        # self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.save_xpath).click()
        # print("New User Created - Rock Paper Scissors")

    # def test_edit_employee(self,booting_function):
    #     self.driver.get(self.url)
    #     time.sleep(5)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_username).send_keys(data.Sahana_Data.username)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_password).send_keys(data.Sahana_Data.password)
    #     self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.login_xpath).click()
    #     time.sleep(3)
    #     self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.pim_xpath).click()
    #     time.sleep(3)
    #     self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.edit_xpath).click()
    #     time.sleep(3)
    #     self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.firstname_edit).send_keys(data.Sahana_Data.input_firstname)
    #     time.sleep(3)
    #     self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.edit_save).click()
    #     print("Edit Successful")

    def test_delete_employee(self,booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_username).send_keys(data.Sahana_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sahana_Selectors.input_password).send_keys(data.Sahana_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.login_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.pim_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.delete_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Sahana_Selectors.confirm_xpath).click()
        print("Employee Deleted Successfully")
        