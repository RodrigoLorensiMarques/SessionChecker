from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


date_today = datetime.now()
date_today_ptbr = date_today.strftime("%d/%m/%Y")


driver = webdriver.Chrome()

driver.get("https://www.surfmappers.com/surfer/p/albums")


search_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Busque por praia, cidade e mais']"))
)

search_input.send_keys("Tramandai")


print(driver.page_source)

today_element = driver.find_elements( By.XPATH,f"//span[contains(normalize-space(.), '{date_today_ptbr}')]"
)


if today_element:
    print("Veja as sessoes de hoje no SurfMappers")


else:
    print("Nada de fotos por hoje!")



