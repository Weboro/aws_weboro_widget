from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://clickconsultingnepal.com/scrape/googlescraper?place_id=ChIJUW-zCOkZ6zkRnadg7FRw22s")

# divs = driver.find_elements_by_tag_name('div')

# Print the text content of each div

sleep(2)

# Close the browser
driver.quit()
