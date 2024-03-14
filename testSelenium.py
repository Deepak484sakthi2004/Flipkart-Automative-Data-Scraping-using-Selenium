from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize a browser driver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a file in append mode to store the scraped data
file_name = "scraped_data.txt"
with open(file_name, "a") as file:
    # Function to scrape the current page
    def scrape_page():
        # Wait for the elements to be present
        try:
            elements = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "_13oc-S"))
            )
            for element in elements:
                file.write(f"{element.text}\n{'**'*20}\n")
                
        except TimeoutException:
            print("Timeout: Unable to locate elements")
            driver.quit()
            exit()


    data = input("ENTER THE ENTITY")
    # Open a website
    driver.get("https://www.flipkart.com/")

    title = driver.title
    print(f"Name of the website is : {title}")

    # Wait for the input field to be present
    try:
        input_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Pke_EE"))
        )
    except TimeoutException:
        print("Timeout: Unable to locate the input field")
        driver.quit()
        exit()

    # Input the data into the search bar

    input_field.send_keys(data)
    input_field.send_keys(Keys.RETURN)

    # Locate the "Next" button
    next_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "_1LKTO3"))
    )

    i = 0
    while True:
        try:
            # Wait for the new page to load
            time.sleep(2)  # Adjust the time as needed

            # Scrape the current page
            scrape_page()
            i += 1
            print(f"Page {i}")

            # Click on the "Next" button
            next_button.click()

        except TimeoutException:
            print("No more pages available.")
            break

# Close the browser
driver.quit()

