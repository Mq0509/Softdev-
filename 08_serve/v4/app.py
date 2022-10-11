'''
M&(I)M: Matthew Yee, Ian Jiang, May Qiu
SoftDev
K08 -- Flask test 4
2022-10-06
time spent: 0.1 hours
'''


from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

# Prediction: Will print "the __name__ of this module is... " and "__main__" to the console,
# open a browser page that has "No hablo queso!" printed on it.
# Run results: Actual behavior was same as predicted behavior.
