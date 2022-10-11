'''
M&(I)M: Matthew Yee, Ian Jiang, May Qiu
SoftDev
K08 -- Flask test1
2022-10-06
time spent: 0.1 hours
'''


from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

# Prediction: app.run() will lead to an empty browser page.
# After running: app.run() opened a browser page with "No hablo queso!" printed on it.
