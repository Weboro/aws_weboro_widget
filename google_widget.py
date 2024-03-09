from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep



class GoogleWidget:

    def __init__(self,Domain):
        
        self.Domain = Domain

        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')  # Enable headless mode
        self.chrome_options.add_argument('--no-sandbox')  # Disable sandbox mode (not recommended for security reasons)
        self.chrome_options.add_argument('--disable-dev-shm-usage')



        self.driver = webdriver.Chrome(options=self.chrome_options)


    def get_data(self,key,user_api_key,place_id):

        # print(f"{self.Domain}/api/scrape/googlescraper?key={key}&user_api_key={user_api_key}&place_id={place_id}")

        self.driver.get(f"{self.Domain}/api/scrape/googlescraper?key={key}&user_api_key={user_api_key}&place_id={place_id}")

        sleep(2)

        divs = self.driver.find_elements(By.XPATH,'//div[@class="reviews-container"]/div')

        # Create a nested array to store the results
        nested_array = []

        # Iterate over each div element
        for div in divs:
            # Find all the p elements inside the div
            p_tags = div.find_elements(By.TAG_NAME,'p')
            
            # Extract the text content of each p element and store in a dictionary
            p_dict = {}
            for p_tag in p_tags:
                class_name = p_tag.get_attribute('class')
                text_content = p_tag.text
                p_dict[class_name] = text_content
            
            # Append the dictionary to the nested array
            nested_array.append(p_dict)

        # Print the nested array
        return nested_array


    def close(self):
        # Close the browser
        self.driver.quit()