from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Konfiguracja opcji dla Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  #max size of window
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")


#inicjalizacja przegladarki
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)


#otworz strone
driver.get("https://www.duckduckgo.com")


#poczekaj na pole do wyszukiwania
search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "q"))
)
search_box.click()
search_box.send_keys("AGH University") #wpisz fraze
search_box.send_keys(Keys.RETURN) #nacisnij enter


#pobierz wyniki
results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3")) #tytuly
)
for i,result in enumerate(results,1):
    print(f"{i}. {result.text}")

driver.quit()