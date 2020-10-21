from selenium import webdriver
import remote_buttons as rb
import scenes

name = "scene 1"

def load_scene(driver):
    response = None

    response = "you are now using google, way better than bing!"

    return response

def input_handler(driver, buttonPressed):
    newScene = None
    response = None

    if buttonPressed == rb.gnrc_act:
        response = "performed generic action"
    elif buttonPressed == rb.toggle_scene:
        driver.get("https://www.bing.com")
        newScene = scenes.sc2
        
    return (newScene, response)