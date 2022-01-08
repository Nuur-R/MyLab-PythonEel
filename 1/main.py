import eel

@eel.expose
def hello():
    print("Hello from Python")
    
eel.init("www")
eel.start("index.html")