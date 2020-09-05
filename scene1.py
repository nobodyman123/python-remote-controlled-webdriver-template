from selenium import webdriver
import remote_buttons as rb
import scenes

name = "scene 1"

def load_scene(driver):
    response = None

    return response

def input_handler(driver, buttonPressed):
    newScene = None
    response = None

    if buttonPressed == rb.gnrc_act:
        response = "performed generic action"
    elif buttonPressed == rb.toggle_scene:
        driver.get("https://www.bing.com")
        newScene = scenes.sc2
        response = "you are now using bing, why would you do this?"
        
    return (newScene, response)