from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import json

username = ""
password = ""

dm_url = "https://www.instagram.com/direct/t/<TRACKING_USER_DM_ID>"

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

while True:
    try:
        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)

        driver.get(dm_url)
        time.sleep(5) 

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Şu an aktif')]")))
            print("Kullanıcı şu an aktif.")

            now = datetime.datetime.now()
            active_time = now.strftime("%Y-%m-%d %H:%M:%S")

            data = {
                "username": "efozdemirx",
                "message": "Kullanıcı şu an aktif.",
                "active_time": active_time
            }

            try:
                with open("active_users.json", "r") as file:
                    existing_data = json.load(file)
            except FileNotFoundError:
                existing_data = []

            existing_data.append(data)
            with open("active_users.json", "w") as file:
                json.dump(existing_data, file, indent=4)

        except:
            print("Kullanıcı şu anda aktif değil.")

    except Exception as e:
        print(f"Hata: {e}")

    finally:
        if 'driver' in locals():
            driver.quit()

        time.sleep(60)
