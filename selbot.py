from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from time import sleep


def vote():

    driver = webdriver.Firefox(executable_path=".\webdrivers\geckodriver.exe")
    #driver = webdriver.Chrome()
    wait = ui.WebDriverWait(driver, 10)
    driver.get('https://poll.fm/11107997')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="PDI_answer50906961"]').click()
    sleep(3)
    """"
    sleep(1)
    driver.execute_script("window.scrollTo(0, 2000)")
    sleep(4)
    wait.until(lambda driver: driver.find_element_by_id('PDI_answer50387147'))
    driver.find_element(By.XPATH, '//*[@id="PDI_answer50387147"]').click()
    sleep(2)
    """
    driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div/div/div/main/form/div[3]/div/a').click()
    driver.close()

if __name__ == "__main__":
    vote()
