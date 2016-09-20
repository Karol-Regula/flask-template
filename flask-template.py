from flask import Flask

app = Flask(__name__) #"app" is just a variable name, can be anything


@app.route("/")
def printer():
    return "Hello, you can choose from routes a, b, and c."

@app.route("/a")
def printera():
    return "Hello, this is route a."

@app.route("/b")
def printerb():
    return "Hello, this is route b."

@app.route("/c")
def printerc():
    return "Hello, this is route c."

if __name__ == '__main__':  #will not print if imported as module
    app.run()
