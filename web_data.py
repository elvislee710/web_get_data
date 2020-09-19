from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time

def get_data(url, path_code):
    home = url
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\alanlee\AppData\Local\Programs\Python\Python38\chromedriver.exe")
    driver.get(home)
    wait = ui.WebDriverWait(driver, 10)
    wait.until(
        lambda driver: driver.find_element_by_xpath(path_code))
    last_trade = driver.find_element_by_xpath(path_code).text
    driver.quit()
    return last_trade
