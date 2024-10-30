from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get(f"https://www.saucedemo.com/")
driver.fullscreen_window()
time.sleep(2)

username_field = driver.find_element(By.NAME, "user-name")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.NAME, "login-button")
login_button.click()

time.sleep(2)

buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for button in buttons:
    # print(button.text)
    time.sleep(1)
    button.click()

cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart.click()


time.sleep(2)

# cart_items = driver.find_elements(By.XPATH, "//div[@class='cart_list']//div")
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
product_title=[]
product_des=[]
product_price=[]
product_image=[]
for i in range(3,9):
    # print(cart_item.text)
    # content=cart_item.find_element(By.CLASS_NAME, "cart_item_label")
    content=driver.find_element(By.XPATH, f"/html/body/div/div/div/div[2]/div/div[1]/div[{i}]/div[2]")
    content.find_element(By.XPATH, f"/html/body/div/div/div/div[2]/div/div[1]/div[{i}]/div[2]/a").click()
    #i=i+1
    time.sleep(2)

    product_name = driver.find_element(By.XPATH, "//*[@id='inventory_item_container']/div/div/div[2]/div[1]")
    product_description = driver.find_element(By.XPATH, "//*[@id='inventory_item_container']/div/div/div[2]/div[2]")
    product_cost = driver.find_element(By.XPATH, "//*[@id='inventory_item_container']/div/div/div[2]/div[3]")
    product_image_link=driver.find_element(By.XPATH, "//*[@id='inventory_item_container']/div/div/div[1]/img")

    product_title.append(product_name.text)
    product_des.append(product_description.text)
    product_price.append(product_cost.text)
    product_image.append(product_image_link.get_attribute("src"))


    # print(product_name.text)
    # print(product_description.text)
    # print(product_cost.text)
    # print(product_image_link.get_attribute("src"))
    back_to_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    back_to_cart.click()
    # driver.back()
    time.sleep(2)


pd.DataFrame({"Product Name":product_title, "Description":product_des, "Price":product_price, "Image Link":product_image}).to_csv("products.csv")
input("Press enter to continue...")


driver.close()


# //*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]
# //*[@id="cart_contents_container"]/div/div[1]/div[4]

# //*[@id="inventory_item_container"]/div/div/div[2]/div[1]

# //*[@id="item_4_title_link"]/div
# //*[@id="item_0_title_link"]/div


# /html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div
# /html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/a/div












