from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')  # Enable headless mode
chrome_options.add_argument('--no-sandbox')  # Disable sandbox mode (not recommended for security reasons)
chrome_options.add_argument('--disable-dev-shm-usage')

from time import sleep

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://clickconsultingnepal.com/scrape/googlescraper?place_id=ChIJUW-zCOkZ6zkRnadg7FRw22s")

# divs = driver.find_elements_by_tag_name('div')

# Print the text content of each div

sleep(2)

# Close the browser
driver.quit()
