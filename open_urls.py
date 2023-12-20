from selenium import webdriver

# List of URLs
urls = [
    "https://example.com",
    "https://google.com",
    "https://github.com",
    # Include the remaining URLs in the list
]

# Set the path to the Chrome WebDriver
webdriver_path = 'C:\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Set the path to the user data directory
user_data_dir = 'C:\Users\Spring\AppData\Local\Google\Chrome\User Data\Profile 11'

# Create ChromeOptions object
options = Options()

# Set the user data directory
options.add_argument('--user-data-dir=' + user_data_dir)

# Initialize the Chrome driver with options
driver = webdriver.Chrome(executable_path=webdriver_path, options=options)


# Open each URL in a new tab
for url in urls:
    driver.execute_script("window.open('" + url + "', '_blank');")

# After opening all the tabs, you can interact with each tab individually
# For example, you can switch to a specific tab by its index
driver.switch_to.window(driver.window_handles[0])  # Switch to the first tab

# Wait for user input to close the browser
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
