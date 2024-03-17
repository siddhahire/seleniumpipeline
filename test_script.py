from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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

# Flag to track validation status
all_images_valid = True

# Iterate through each image element and check the validity of the image link
for img in image_elements:
    image_src = img.get_attribute('src')
    if image_src:
        # Check if the image source URL has a valid extension
        if not image_src.lower().endswith(('.png', '.jpeg', '.jpg')):
            all_images_valid = False
            print(f"Image link {image_src} does not have a valid image extension.")
            break

# Print "Test Passed" if all images are valid
if all_images_valid:
    print("Test Passed")

# Close the WebDriver
driver.quit()

