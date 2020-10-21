from selenium import webdriver
import remote_buttons as rb
import scenes

name = "universal"

def input_handler(driver, buttonPressed):
    response = None

    if buttonPressed == rb.power:
        driver.quit()
        quit()
    elif buttonPressed == rb.rld:
        response = "reloading page..."
        driver.refresh()
        
    return response