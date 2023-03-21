from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import Globals

# Initialize the browser (this example uses Chrome)          
driver = webdriver.Chrome()

def send_command(command):
    try:
        input_box = driver.find_element(By.ID, 'cmd_s')
    except NoSuchElementException:
        print("Error: Could not find command input box")
        return
    
    # Type the command into the input box
    input_box.send_keys(command)
    time.sleep(1)
    
    try:
        # Press Enter to submit the command
        input_box.send_keys(Keys.RETURN)
        time.sleep(0.5)
    except:
        print("Error: Failed to execute command")

# Open the cueserver webpage
driver.get(Globals.cueserver_ip)



driver.quit()