from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urljoin
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

url = "file:////var/lib/jenkins/workspace/newP/index.nginx-debian.html"  
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Open the web page
driver.get(url)

# Find all image elements on the page
image_elements = driver.find_elements(By.TAG_NAME, 'img')

# Iterate through each image element and check the validity of the image link
for img in image_elements:
    image_src = img.get_attribute('src')
    if image_src:
        # Check if the image source URL has a valid extension
        if image_src.lower().endswith(('.png', '.jpeg', '.jpg')):
            print(f"Test Passed")
        else:
            print(f"Image link {image_src} does not have a valid image extension.")

# Close the WebDriver
driver.quit()
