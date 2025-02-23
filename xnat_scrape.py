import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up argument parser
parser = argparse.ArgumentParser(description="Scrape XNAT instance for specific text.")
parser.add_argument("url", help="XNAT instance login URL")
parser.add_argument("username", help="Username for XNAT login")
parser.add_argument("password", help="Password for XNAT login")
args = parser.parse_args()

# Set up Selenium WebDriver (ensure you have the appropriate driver installed)
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options) # You may use Firefox or Edge as well

driver.get(args.url)

time.sleep(3)  # Wait for the page to load

# Locate and fill the username and password fields
driver.find_element(By.NAME, "username").send_keys(args.username)
driver.find_element(By.NAME, "password").send_keys(args.password, Keys.RETURN)

time.sleep(5)  # Wait for login to complete

# Scrape the specific line
try:
    element = driver.find_element(By.XPATH, "//*[contains(text(), 'XNAT currently contains')]")
    print(element.text)
except Exception as e:
    print("Error finding the element:", e)

# Close the browser
driver.quit()

