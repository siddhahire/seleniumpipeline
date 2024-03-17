from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urljoin

# URL of the web page
url = "http://44.202.135.160/index.html"  # Replace with your URL

# Instantiate WebDriver (Chrome)
driver = webdriver.Chrome()

# Open the web page
driver.get(url)

# Find all image elements on the page
image_elements = driver.find_elements(By.TAG_NAME, 'img')

# Iterate through each image element and check the validity of the image link
for img in image_elements:
    image_src = img.get_attribute('src')
    if image_src:
        full_image_url = urljoin(url, image_src)
        try:
            response = requests.head(full_image_url)  # Send a HEAD request to check if the image link is valid
            if response.status_code == 200:
                print(f"All tests passed")
            else:
                print(f"Image link {full_image_url} is invalid (Status Code: {response.status_code}).")
        except Exception as e:
            print(f"Error occurred while checking image link {full_image_url}: {e}")

# Close the WebDriver
driver.quit()
