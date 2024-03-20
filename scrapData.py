import os
import time
import requests
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

def download_images(search_term, num_images):
    # Set up the Chrome WebDriver
    chrome_options = ChromeOptions()
    # To run Chrome headlessly without UI (remove for visible browser)
    chrome_options.headless = True
    chrome_service = ChromeService(
        executable_path='./', chrome_options=chrome_options)
    driver = webdriver.Chrome(service=chrome_service)

    # Set up the Google Images URL
    url = "https://www.google.com/imghp?hl=en"
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Find the search input and enter the search term
    search_box = driver.find_element("name", "q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for the search results to load

    # Scroll the page to load more images
    loaded_images = 0
    while loaded_images < num_images:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for images to load

        # Find all image elements
        image_elements = driver.find_elements(
            "css selector", "img.rg_i.Q4LuWd")

        # Check the number of new images loaded
        new_images_count = len(image_elements) - loaded_images

        # If no new images loaded, break the loop
        if new_images_count == 0:
            break

        # Create a folder to save the images
        save_folder = search_term.replace(" ", "_")
        os.makedirs(save_folder, exist_ok=True)

        # Download the new images
        for i in range(new_images_count):
            image_element = image_elements[loaded_images + i]
            image_url = image_element.get_attribute('data-src')
            if image_url:
                image_url = image_url.split(",")[0]
                image_name = f"{search_term}_{loaded_images + i + 1}.jpg"
                image_path = os.path.join(save_folder, image_name)

                # Download the image using requests
                response = requests.get(image_url)
                with open(image_path, 'wb') as f:
                    f.write(response.content)

        loaded_images += new_images_count
    driver.quit()


if __name__ == "__main__":
    search_terms = ["kaju katli", "gulab jamun", "peda", "rasmalai", "rasgulla", "besan ke laddu", "jalebi", "balushahi", "soan papdi", "modak"]
    num_images = 600
    pool = multiprocessing.Pool()
    pool.starmap(download_images, [(search, num_images) for search in search_terms])
    pool.close()
    pool.join()


# if you are unable to scrap data then directly downlaod from this link - https://drive.google.com/file/d/1_U6wxKoALszTnXclzL8Fa3Ij8cYL_bVi/view?usp=sharing