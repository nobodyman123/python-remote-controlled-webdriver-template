from http.server import HTTPServer, BaseHTTPRequestHandler
import remote_buttons as rb
from selenium import webdriver
from threading import Thread
import scenes

#import all your scenes here
import scene1
import scene2
    
#driver settings
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driverPath = "chromedriver.exe"
driver = webdriver.Chrome(driverPath, chrome_options=options)
driver.get("https://www.google.com")

scenes_int2imp = [scene1, scene2]

currentScene = scenes_int2imp[0]
currentScene.load_scene(driver)
print("[driver] current scene is " + currentScene.name)

class Handler(BaseHTTPRequestHandler):
    #only un-comment do_GET when testing on local_host
    '''
    def do_GET(self):
        index = open("test.html")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(index.read().encode())
    #'''

    def do_POST(self):
        print("----------")
        
        content_length = int(self.headers['Content-Length'])
        raw_post_data = str(self.rfile.read(content_length))
        post_data = raw_post_data.split("'")[1]

        #post_data = post_data.replace("inp=", "")  #only un-comment this line when testing on localhost

        print("[server] received post request: " + post_data)

        try:
            post_data = int(post_data)
        except:
            post_data = None
        
        if post_data != None:
            response = input_handler(driver, post_data)

        if response != None:
            #self.wfile.write(("resp: " + response).encode()) #only un-comment this line when testing on localhost
            
            self.send_response(200, response)
            print("[server] responded: " + str(response))

def input_handler(driver, buttonPressed):
    response = None

    if buttonPressed == rb.power:
        response = "shutting down..."
        Handler.send_response(200, response)
        driver.quit()
        quit()
    elif buttonPressed == rb.rld:
        response = "reloading page..."
        driver.refresh()
    else:
        global currentScene

        (newScene, response) = currentScene.input_handler(driver, buttonPressed)
        
        if newScene != None:
            currentScene = scenes_int2imp[newScene]
            
            response = currentScene.load_scene(driver)
            print("[driver] switched scene to " + currentScene.name)
    
    return response

#server settings
port = 8080
server_adress = ("0.0.0.0", port)
server = HTTPServer(server_adress, Handler)

serverThread = Thread(target=server.serve_forever)
serverThread.start()
print("[server] server running on port " + str(port))
