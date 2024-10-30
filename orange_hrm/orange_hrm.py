from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(f"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.fullscreen_window()
time.sleep(10)

username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
username_field.send_keys("Admin")
password_field.send_keys("admin123")



# password_field.send_keys(Keys.RETURN)

login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()

driver.fullscreen_window()

try:
    # canvas = driver.find_element(By.CLASS_NAME, "oxd-pie-chart")  
    # children = canvas.find_elements(By.XPATH, "./*")
 
    # for child in children:
    #     child.screenshot("extracted_canvas.png")
 
    # print("Canvas image saved as 'extracted_canvas.png'.")
 
    dropdown = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab")
    dropdown.click()
 
    time.sleep(3)
    logout_button = driver.find_element(By.XPATH, "//a[text()='Logout']")
    logout_button.click()
 
    print("Logout successful")
except:
    print("Unable to save canvas image.")

time.sleep(3)
input("Press Enter to continue...")
driver.close()