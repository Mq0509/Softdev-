M&(I)M: Matthew Yee, Ian Jiang, May Qiu
SoftDev
K11 -- Flask Forms
2022-10-16
time spent: 0.5 hours

app.py notes:
Prediction: disp_loginpage and authenticate will print the DIAG strings into the terminal.
            The browser will prompt the user for a username, and once that is provided, "Waaaa hooo HAAAH" will be rendered.

When running app.py with print(request.args['username']) uncommented, an error is produced stating 'username' is recognized.
When uncommenting , methods=['POST,'GET']) will result in no changes. Leaving only 'GET' within the brackets also does nothing. 
Having only 'POST' will result in an error saying that the method is not allowed for the requested URL for both disp_loginpage() and authenticate()

login.html notes:

form action

input type = "text" signifies that the browser will take text input from the user
input type = "submit" signifies that the browser will have a button to submit the user's text input.
