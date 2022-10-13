app.py:
Prediction: app.run would print "the __name__ of this module is... " and "__main__" to the console and open a browser page that has "No hablo queso!" printed on it.
Results: Same as prediction.

foo:
Prediction: accessing foo via http://localhost:5000/static/foo would cat the contents of foo into a browser page.
Results: Opened a blank browser page that downloaded foo as a plaintext file.

foo.html:
Prediction: Opens a browser page with "Is this plaintext, though?" printed on it. 
Results: Same a prediction.

Notes: app.py had to be running in the terminal in order for foo and foo.html to render in the browser.
