from http.server import HTTPServer, BaseHTTPRequestHandler
import remote_buttons as rb
from selenium import webdriver
from threading import Thread
import universal
import scenes
import debug

#import all your scenes here
import scene1
import scene2
    
#driver settings
OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument('--ignore-certificate-errors')
OPTIONS.add_argument('--ignore-ssl-errors')

DRIVERPATH = "chromedriver.exe"
DRIVER = webdriver.Chrome(DRIVERPATH, options=OPTIONS)
START_URL = "https://www.google.com"

#put in your scenes here (using the value in scenes.py as index for each scene)
scenes_int2imp = [scene1, scene2]

currentScene = scenes_int2imp[0]
currentScene.load_scene(DRIVER)
debug.log(f"current scene is {currentScene.name}", "driver")

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

        debug.log(f"received post request: {post_data}", "server")

        try:
            post_data = int(post_data)
        except:
            post_data = None
        
        if post_data != None:
            response = input_handler(DRIVER, post_data)

        if response != None:
            #self.wfile.write(("resp: " + response).encode()) #only un-comment this line when testing on localhost
            
            self.send_response(200, response)
            debug.log(f"responded: {response}", "server")

def input_handler(driver, buttonPressed):
    response = None

    if (response := universal.input_handler(DRIVER, buttonPressed)):
        pass
    else:
        global currentScene

        (newScene, response) = currentScene.input_handler(DRIVER, buttonPressed)
        
        if newScene != None:
            currentScene = scenes_int2imp[newScene]
            
            response = currentScene.load_scene(DRIVER)
            debug.log(f"switched scene to {currentScene.name}", "driver")
    
    return response

#server settings
PORT = 8080
SERVER_ADRESS = ("0.0.0.0", PORT)
SERVER = HTTPServer(SERVER_ADRESS, Handler)

if __name__ == "__main__":
    DRIVER.get(START_URL)

    serverThread = Thread(target=SERVER.serve_forever)
    serverThread.start()
    debug.log(f"server running on port {PORT}", "server")