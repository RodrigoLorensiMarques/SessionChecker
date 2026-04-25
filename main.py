from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time


date_today = datetime.now()
date_today_ptbr = date_today.strftime("%d/%m/%Y")


driver = webdriver.Chrome()

driver.get("https://www.surfmappers.com/surfer/p/albums")


search_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Busque por praia, cidade e mais']"))
)

search_input.send_keys("Tramandai")
time.sleep(2)
search_input.send_keys(Keys.RETURN)


WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//section[contains(@class,'grid')]//div[contains(@class,'rounded-2xl')]"))
)
time.sleep(2)

today_element = driver.find_elements( By.XPATH,f"//section[contains(@class,'grid')]//span[starts-with(normalize-space(.), '{date_today_ptbr}')]"
)


if today_element:
    print(f"Veja as sessoes de hoje ({date_today_ptbr}) no SurfMappers")

    for el in today_element:
        try:
            card = el.find_element(By.XPATH, "./ancestor::div[contains(@class,'rounded-2xl')]")
            beach = card.find_element(By.TAG_NAME, "h3").text
            print(f"   {beach} — {el.text}")
        except:
            print(f"   {el.text}")



