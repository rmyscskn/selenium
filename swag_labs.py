from doctest import TestResults
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 


class Swag_labs:
    def __init__(self):
        self.driver=webdriver.Chrome()
    
    def giris(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,'user-name')
        passwordInput = driver.find_element(By.ID,'password')
        sleep(2)
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID,'login-button')
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
       
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
        
    def bosgecis(self):
        print(f"TEST SONUCU: {TestResults}") 
        
    def gecis(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,'user-name')
        passwordInput = driver.find_element(By.ID,'password')
        sleep(2)
        userNameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,'login-button')
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
       
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")  
         
    def gecis1(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,'user-name')
        passwordInput = driver.find_element(By.ID,'password')
        sleep(2)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,'login-button')
        loginButton.click()
        sleep(2)

        products = driver.find_elements(By.CLASS_NAME, 'inventory_item_description')
        print(f" {len(products)} adet ürün vardır")

        sleep(5)
           
testClass = Swag_labs()
testClass.giris()
testClass.bosgecis()
testClass.gecis()
testClass.gecis1()