'''
M&(I)M: Matthew Yee, Ian Jiang, May Qiu
SoftDev
K08 -- Flask test 3
2022-10-06
time spent: 0.1 hours
'''


from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

# Prediction: Will print "about to print __name__..." in the console along with "__main__"
# and open a broswer page with "No hablo queso!" printed on it.
# Run results: Prints "Serving Flask app 'app'" and "Debug mode: on" to the console,
# and broswer page no longer opens.
