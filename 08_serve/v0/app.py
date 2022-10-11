'''
M&(I)M: Matthew Yee, Ian Jiang, May Qiu
SoftDev
K08 -- Flask test 0
2022-10-06
time spent: 0.1 hours
'''

# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # We have seen similar syntax in Java, where functions are called using parentheses.
                      # Calls the main function of the flask module.


@app.route("/") # '/' in app.route could be referring to the root directory, specifically, the highest
                # directory which we have access to.
def hello_world():
    print(__name__) # The print statement would print to the console.
                    # The print statement would print the results of running app.
    return "No hablo queso!"  #"No hablo queso!" would have to appear in the browser, because it is the result of
                              # running app, and that result gets printed to the browser.

app.run()  # We may have seen similar constructs in html.

# Prediction: app.run() opens a browser page with "No hablo queso!" printed on it.
# Run results: app.run() opens a browser page with "No hablo queso!" printed on it,
# along with printing "__main__" to the console.
