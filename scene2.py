from selenium import webdriver
import remote_buttons as rb
import scenes

name = "scene 2"

def load_scene(driver):
    response = None

    response = "you are now using bing, why would you do this?"

    return response

def input_handler(driver, buttonPressed):
    newScene = None
    response = None

    if buttonPressed == rb.toggle_scene:
        driver.get("https://www.google.com")
        newScene = scenes.sc1

    return (newScene, response)